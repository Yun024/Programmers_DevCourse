from airflow import DAG
from airflow.decorators import task
from airflow.providers.amazon.aws.transfers.sql_to_s3 import SqlToS3Operator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

from datetime import datetime
from datetime import timedelta

import logging


def get_snowflake_connection():
    hook = SnowflakeHook(snowflake_conn_id='snowflake_dev_db')
    return hook.get_conn().cursor()

def get_s3_credentials():
    aws_hook = S3Hook(aws_conn_id="aws_conn_id")
    credentials = aws_hook.get_credentials()
    aws_access_key = credentials.access_key
    aws_secret_access_key = credentials.secret_key
    return aws_access_key, aws_secret_access_key


def create_mysql_to_s3_task(dag, s3_bucket, s3_key):
    return SqlToS3Operator(
        task_id='mysql_to_s3_nps',
        query = "SELECT * FROM prod.nps WHERE DATE(created_at) = DATE('{{ execution_date }}')",
        s3_bucket=s3_bucket,
        s3_key=s3_key,
        sql_conn_id="mysql_conn_id",
        aws_conn_id="aws_conn_id",
        verify=False,
        replace=True,
        pd_kwargs={"index": False, "header": False},
    )

def create_sql(cur, schema, table, drop_first, temporary=False):
    temp_suffix = "_temp" if temporary else ""
    table_name = f"{table}{temp_suffix}"
    if drop_first:
        cur.execute(f"DROP TABLE IF EXISTS {schema}.{table_name}")
    table_type = "TEMPORARY TABLE" if temporary else "TABLE"
    cur.execute(f"""
    CREATE {table_type} {schema}.{table_name} (
        id INT NOT NULL PRIMARY KEY,
        created_at TIMESTAMP,
        score SMALLINT
    );
    """)


def merge_sql(cur, schema, table):
    cur.execute(f"""
    MERGE INTO {schema}.{table} AS target
    USING {schema}.{table}_temp AS staging
    ON target.id = staging.id
    WHEN MATCHED THEN
        UPDATE SET
            created_at = staging.created_at,
            score = staging.score
    WHEN NOT MATCHED THEN
        INSERT (id, created_at, score)
        VALUES (staging.id, staging.created_at, staging.score);
    """)

def copy_sql(cur,schema,table, s3_bucket, s3_key, access_key, secret_key):
    cur.execute(f"""
COPY INTO dev.{schema}.{table}_temp
FROM 's3://{s3_bucket}/{s3_key}'
credentials = (AWS_KEY_ID='{access_key}' AWS_SECRET_KEY='{secret_key}')
FILE_FORMAT = (type='csv')
;""")


@task
def s3_to_snowflake(schema, table, s3_bucket, s3_key):
    cur = get_snowflake_connection()
    access_key, secret_key = get_s3_credentials()
    try:
        cur.execute("BEGIN;")
        create_sql(cur, schema, table, False, True)
        copy_sql(cur, schema, table, s3_bucket, s3_key, access_key, secret_key)
        merge_sql(cur,schema,table)
        cur.execute("COMMIT;")

    except Exception as error:
        print(error)
        cur.execute("ROLLBACK;")
        raise
    logging.info("s3_to_snowflake done")


with DAG(
    dag_id = 'MySQL_to_Snowflake',
    start_date = datetime(2022,8,24), # 날짜가 미래인 경우 실행이 안됨
    schedule = '0 9 * * *',  # 적당히 조절
    max_active_runs = 1,
    catchup = False,
    default_args = {
        'retries': 1,
        'retry_delay': timedelta(minutes=3),
    }
) as dag:
    
    schema = "yeojun"
    table = "nps"
    s3_bucket = "yeojun-test-bucket"
    s3_key = schema + "-" + table
    
    mysql_to_s3_nps = create_mysql_to_s3_task(dag, s3_bucket, s3_key)
    
mysql_to_s3_nps >> s3_to_snowflake(schema, table, s3_bucket, s3_key)