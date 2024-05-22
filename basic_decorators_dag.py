from airflow.decorators import dag, task
from datetime import datetime

@dag(start_date = datetime(2024,5,1), 
     schedule='@once'
     )

def basic_decorators_dag():

    @task(retries=3)
    def start():
        return "success"
    
    @task.branch
    def choose_task(next_task: str):
        return next_task
    
    @task
    def success():
        print("success")

    @task(retries=1)
    def failure():
        print("failure")    

    choose_task(start()) >> [success(), failure()]   

basic_decorators_dag()    
