from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator

def get_last_dag_run(dag):
    last_dag_run = dag.get_last_dagrun()

    if last_dag_run is None:
        return '2021-01-01'
    else:
        return last_dag_run.execution_date.strftime("%Y-%m-%d")

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2021, 3, 21),
    'retries': 1,
    'retry_delay': timedelta(seconds=30)
}

CMD = "echo {}"
with DAG(
    dag_id='testing_variables', 
    default_args=default_args, 
    schedule_interval='@daily', 
    catchup=False, 
    user_defined_macros={
          'last_dag_run_execution_date': get_last_dag_run
      }) as dag:

    date = BashOperator(
        task_id="date",
        bash_command="echo {{ last_dag_run_execution_date(dag) }}"
    )

    date