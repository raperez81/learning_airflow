# based on: https://airflow.apache.org/docs/apache-airflow/1.10.12/tutorial.html

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['raperez81@hotmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    'sla': timedelta(seconds=5)
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

with DAG("default_arguments_dag",
         start_date = datetime(2024, 5, 1),
         schedule = "@daily",
         default_args = default_args,
         catchup = False):

    t1 = BashOperator(
        task_id = "print_date",
        bash_command = "date"
        )

    t2 = BashOperator(
        task_id = "sleep",
        bash_command = "sleep 10" #sleep 5 seconds
        )
    # @task
    # def print_default_arguments():
    #     print("default_arguments:")

    t1 >> t2
