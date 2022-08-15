from airflow import DAG
from datetime import datetime,timedelta, date
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import sys
import syslog
import os
import pandas as pd
import json
print(os.path.abspath("working.............................."))
sys.path.append(os.path.abspath("includes/python"))

from extract_data import Extractor
from loader import Loader
DBT_PROJECT_DIR = "~/traffic_dbt"
DBT_PROFILE_DIR = "~/traffic_dbt/.dbt"
extract = Extractor()
loader = Loader()

def run_extractor(**context):
    sample = extract.load_csv("~/data/20181024_d1_0830_0900.csv")
    cleaned = extract.transform_raw_data(sample)
    path = extract.get_file_path(datetime.today())
    cleaned.to_csv(path, index=False)
    context['ti'].xcom_push(key='dataframe', value=path)
    print(cleaned.iloc[1,1])

def run_loader(**context):
    path = context['ti'].xcom_pull(key='dataframe')
    data = extract.load_csv(path)
    print(f"..................  {data.columns}")
    try:
        conn, cur = loader.connect_to_server(host="postgres", port=5432, user="warehouse", password="warehouse", dbName="warehouse")
        loader.create_table(cur, "includes/sql/create_table.sql", "warehouse")
        loader.insert_into_table(cur, conn, "warehouse", data, "traffic_flow")
        loader.close_connection(cur, conn)
    except Exception as e:
        print(f"error...: {e}")
    
    


default_args = {"owner":"airflow","start_date":datetime(2021,3,7)}
with DAG(dag_id="workflow",default_args=default_args,schedule_interval='@daily', catchup=False) as dag:
   
    extract_task= PythonOperator(
        task_id = "extract_task",
        python_callable = run_extractor,
        provide_context=True
        )
    load_task = PythonOperator(
        task_id = "load_task",
        python_callable = run_loader,
        provide_context=True
        )
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd ~/traffic_dbt && ~/.local/bin/dbt run --profiles-dir {DBT_PROFILE_DIR}",
    )
    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd ~/traffic_dbt && ~/.local/bin/dbt test --profiles-dir {DBT_PROFILE_DIR}",
    )
    dbt_doc = BashOperator(
        task_id="dbt_doc",
        bash_command=f"cd ~/traffic_dbt && ~/.local/bin/dbt docs generate --profiles-dir {DBT_PROFILE_DIR} && ~/.local/bin/dbt docs serve --port 7211 --profiles-dir {DBT_PROFILE_DIR}",
    )
extract_task >> load_task >> dbt_run >> dbt_test >> dbt_doc