import airflow
from airflow import DAG
from datetime import datetime

#Create and instance of a DAG class
with DAG(
    dag_id="traffic_flow_dag",
    schedule_interval="@daily", 
    start_date=airflow.utils.dates.days_ago(1),
    catchup=False,
) as dag:

