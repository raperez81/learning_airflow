from airflow.decorators import dag, task
from datetime import datetime

@dag(start_date=datetime(2022, 1,1), 
     schedule = '@daily')

def two_tasks_dag_taskflow():

    @task
    def start():
        return 42
    
    @task
    def get_val(val: int):
        print(val)
    
    get_val(start())

two_tasks_dag_taskflow()
