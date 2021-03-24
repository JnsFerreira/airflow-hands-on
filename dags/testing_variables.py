from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

def get_last_dag_run():
    return "some_value"

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2021, 3, 21),
    'retries': 1,
    'retry_delay': timedelta(seconds=30)
}


with DAG(
    dag_id='testing_variables', 
    default_args=default_args, 
    schedule_interval='@daily', 
    catchup=True, 
    user_defined_macros={
          'last_dag_run_execution_date': get_last_dag_run
      }
) as dag:

    my_bash = BashOperator(
        task_id="date",
        bash_command="echo SELECT * FROM  my_table WHERE date >= {{ last_dag_run_execution_date() }}"
    )

    my_bash