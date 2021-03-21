from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2021, 3, 20),
    'retries': 1,
    'retry_delay': timedelta(seconds=30)
}

with DAG(
    dag_id='store_sales', 
    default_args=default_args, 
    schedule_interval='@daily', 
    catchup=False) as dag:

    check_if_file_exists = BashOperator(
        task_id = "check_if_file_exists",
        bash_command="shasum ~/store_files_airflow/raw_store_transactions.csv",
        retries=2,
        retry_dalay=timedelta(seconds=5)
    )

    check_if_file_exists
