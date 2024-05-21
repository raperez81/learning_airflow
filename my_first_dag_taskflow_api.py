from airflow.decorators import dag, task
from datetime import datetime

@dag(start_date=datetime(2023, 1, 1),
     description='A simple tutorial DAG', 
     tags=['data_science'], 
     schedule='@daily', 
     catchup=False)
def my_first_dag_taskflow_api():
    
    @task
    def print_a(name):
        print(f"hi {name} from task a")

    print_a("Ricardo")

my_first_dag_taskflow_api()
