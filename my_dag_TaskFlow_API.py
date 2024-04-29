from airflow.decorators import dag, task
from datetime import datetime

@dag(start_date=datetime(2023, 1, 1), description='A simple tutorial DAG', 
     tags=['data_science'], schedule='@daily', catchup=False)
def my_dag():
    
    @task
    def print_a():
        print('hi from task a')
