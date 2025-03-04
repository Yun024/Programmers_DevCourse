from airflow import DAG
from airflow.models import Variable
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.decorators import task

from datetime import datetime
from datetime import timedelta

import requests
import logging
import json


def get_snowflake_connection():
    # autocommit is False by default
    hook = SnowflakeHook(snowflake_conn_id='snowflake_dev_db')
    return hook.get_conn().cursor()

@task
def etl(schema, table):
    api_key = Variable.get("open_weather_api_key")
    # 서울의 위도/경도
    lat = 37.5665
    lon = 126.9780

    # https://openweathermap.org/forecast5
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)

    """
    {"cod":"200","message":0,"cnt":40,"list":[{"dt":1661871600,"main":{"temp":296.76,"feels_like":296.98,"temp_min":296.76,"temp_max":297.87,"pressure":1015,"sea_level":1015,"grnd_level":933,"humidity":69,"temp_kf":-1.11},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":100},"wind":{"speed":0.62,"deg":349,"gust":1.18},"visibility":10000,"pop":0.32,"rain":{"3h":0.26},"sys":{"pod":"d"},"dt_txt":"2022-08-30 15:00:00"},
    
    {"dt":1661882400,"main":{"temp":295.45,"feels_like":295.59,"temp_min":292.84,"temp_max":295.45,"pressure":1015,"sea_level":1015,"grnd_level":931,"humidity":71,"temp_kf":2.61},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":96},"wind":{"speed":1.97,"deg":157,"gust":3.39},"visibility":10000,"pop":0.33,"rain":{"3h":0.57},"sys":{"pod":"n"},"dt_txt":"2022-08-30 18:00:00"},
    
    {"dt":1662292800,"main":{"temp":294.93,"feels_like":294.83,"temp_min":294.93,"temp_max":294.93,"pressure":1018,"sea_level":1018,"grnd_level":935,"humidity":64,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":{"all":88},"wind":{"speed":1.14,"deg":17,"gust":1.57},"visibility":10000,"pop":0,"sys":{"pod":"d"},"dt_txt":"2022-09-04 12:00:00"}],"city":{"id":3163858,"name":"Zocca","coord":{"lat":44.34,"lon":10.99},"country":"IT","population":4593,"timezone":7200,"sunrise":1661834187,"sunset":1661882248}}
    """
    ret = []
    for d in data["list"]:
        day = datetime.fromtimestamp(d["dt"]).strftime('%Y-%m-%d %H')
        ret.append("('{}',{},{},{},GETDATE())".format(day, d["main"]["temp"], d["main"]["temp_min"], d["main"]["temp_max"]))

    cur = get_snowflake_connection()
    drop_sql = f"DROP TABLE IF EXISTS {schema}.{table};"
    create_sql = f"""
CREATE TABLE {schema}.{table} (
    date datetime,
    temp float,
    min_temp float,
    max_temp float,
    created_date timestamp default GETDATE()
);
"""
    insert_sql = f"""INSERT INTO {schema}.{table} VALUES """ + ",".join(ret)
    logging.info(drop_sql)
    logging.info(create_sql)
    logging.info(insert_sql)
    try:
        cur.execute(drop_sql)
        cur.execute(create_sql)
        cur.execute(insert_sql)
        cur.execute("Commit;")
    except Exception as e:
        cur.execute("Rollback;")
        raise

with DAG(
    dag_id = 'Weather_to_snowflake',
    start_date = datetime(2023,5,30), # 날짜가 미래인 경우 실행이 안됨
    schedule = '0 2 * * *',  # 적당히 조절
    max_active_runs = 1,
    catchup = False,
    default_args = {
        'retries': 1,
        'retry_delay': timedelta(minutes=3),
    }
) as dag:

    etl("yeojun", "weather_forecast")
