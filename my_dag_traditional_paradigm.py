from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

def print_a():
    print('hi from task a')

with DAG('my_dag', start_date=datetime(2023, 1 , 1),
         description='A simple tutorial DAG', tags=['data_science'],
         schedule='@daily', catchup=False):
    
    task_a = PythonOperator(task_id='task_a', python_callable=print_a)
