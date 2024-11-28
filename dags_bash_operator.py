from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id="example_bash_operator",
    start_date=datetime(2024, 11, 28)
    schedule_interval="@daily",
    catchup=False    
) as dag: