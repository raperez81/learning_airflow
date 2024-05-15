from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import get_current_context
import pendulum
from datetime import date, datetime, timedelta

with DAG(
   'backfilling_dag',
   schedule = '0/2 * * * *',
   start_date = pendulum.datetime(2023,3,1),
   catchup = True
):
    @task
    def task1():
        context = get_current_context()

        data_interval_start = context["data_interval_start"]
        data_interval_end = context["data_interval_end"]
        time_delta = timedelta(minutes=1)
        print("data_interval_start:", context["data_interval_start"])
        print("data_interval_end:", context["data_interval_end"])
        
        # print every minute between data_interval_start and data_interval_end
        date_to_print = data_interval_start
        print("date_to_print:", date_to_print)
        while date_to_print < data_interval_end:
            date_to_print = date_to_print + time_delta
            print("date_to_print:", date_to_print)

    task1()
