from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy import DummyOperator

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2021, 3, 22),
    'retries': 1,
    'retry_delay': timedelta(seconds=30)
}

with DAG(
    dag_id='cycle_error',
    default_args=default_args,
    schedule_interval='None'
) as dag:
    t1 = DummyOperator(task_id='t1')
    t2 = DummyOperator(task_id='t2')
    t3 = DummyOperator(task_id='t3')

    t1 >> t2 >> t3 >> t1
