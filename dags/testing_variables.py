from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

def get_start_date(base_date):
    return 'start_date'

def get_end_date(base_date):
    return 'end_date'

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2021, 3, 22),
    'retries': 1,
    'retry_delay': timedelta(seconds=30)
}

with DAG(
    dag_id='testing_variabl5', 
    default_args=default_args, 
    schedule_interval='@daily', 
    catchup=True, 
    user_defined_macros={
          'start_date' : get_start_date,
          'retireve_end_date' : get_end_date 
      }
) as dag:

    my_bash = BashOperator(
        task_id="GET",
        bash_command="echo {{ retireve_end_date( prev_execution_date_success )}} maior que {{ start_date( ds ) }}"
    )

    my_bash