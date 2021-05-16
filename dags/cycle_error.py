from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

with DAG() as dag:
    t1 = DummyOperator(task_id='t1')
    t2 = DummyOperator(task_id='t2')
    t3 = DummyOperator(task_id='t3')

    t1 >> t2 >> t3 >> t1
