from airflow.decorators import dag, task
from datetime import datetime

@dag(start_date=datetime(2023, 1, 1),
     description='A simple tutorial DAG', 
     tags=['data_science'], 
     schedule='@daily', 
     catchup=False)
def my_dag_taskflow_api():
    
    @task
    def print_a():
        print('hi from task a')

    print_a()

my_dag_taskflow_api()
