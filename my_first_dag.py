from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

def print_a():
    print('Hi from task_a')
    
with DAG('my_first_dag', 
         start_date=datetime(2023, 1, 1), 
         description='A simple tutorial DAG',
         schedule='@daily', 
         tags=['data_science'],
         catchup=False):

    task_a = PythonOperator(task_id='task_a', python_callable=print_a)



