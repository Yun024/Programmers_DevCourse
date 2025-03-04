from airflow import DAG
from airflow.decorators import task
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.models import Variable

from datetime import datetime
import pandas as pd
import logging
import requests

def get_snowflake_connection(autocommit=True):
    hook = SnowflakeHook(snowflake_conn_id="snowflake_dev_db")
    conn = hook.get_conn()
    conn.autocommit = autocommit
    return conn.cursor()

@task
def extract(url):
    logging.info(datetime.utcnow())
    countries = requests.get(url).json()
    return countries

@task
def transform(countries):
    records = []
    for country in countries:
        name = country['name']['official']
        area = country['area']
        population = country['population']
        records.append([name,area, population])
    logging.info("Transform ended")
    return records


@task
def load(schema, table, records):
    logging.info("load started")
    cur = get_snowflake_connection()
    """
    records = [
        ["Korea", "30" "5000"],
        ["USA", "100", "15000"],
        ...
    ]
    """

    try:
        cur.execute("BEGIN;")
        cur.execute(f"DROP TABLE IF EXISTS {schema}.{table};")
        cur.execute(f"""
CREATE TABLE {schema}.{table} (
    name varchar,
    area float,
    population number
);""")
        for r in records:
            sql = f"INSERT INTO {schema}.{table} VALUES(%s, %s, %s);"
            cur.execute(sql, r)
            print(sql)
        cur.execute("COMMIT;")
    except Exception as error:
        print(error)
        cur.execute("ROLLBACK;")
        raise

    logging.info("laod done")


with DAG(
    dag_id = "Restcountries",
    start_date = datetime(2025,1,15),
    catchup=False,
    tags=['API'],
    schedule= "30 6 * * 6"
) as dag:

    url = Variable.get("Restcountry_url")
    schema = "yeojun"
    table = "country_info"

    country_list = transform(extract(url))
    load(schema, table, country_list)


