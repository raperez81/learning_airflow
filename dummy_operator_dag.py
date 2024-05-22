from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(dag_id = "dummy_operator_dag",
         start_date = datetime(2024, 5, 1),
         schedule = None
         ):

    @task
    def start_task():
        pass

    @task
    def task_1a():
        pass

    @task
    def task_1b():
        pass

    @task
    def task_1c():
        pass


    @task
    def task_2():
        pass

    @task
    def end_task():
        pass

    start_task() >> [task_1a(), task_1b(), task_1c()] >> task_2() >> end_task()

