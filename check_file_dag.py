from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

with DAG(dag_id='check_dag',
        start_date=datetime(2023, 1, 1), 
        description='DAG to check data', 
        tags=['data_engineering'], 
        # every 5 minutes
        schedule='0/5 * * * *', 
        # every 3 days
        #schedule_interval=timedelta(days=3),
        catchup=False):
    
    create_file = BashOperator(
        task_id='create_file',
        bash_command='echo "Hi there!" >/tmp/dummy.txt'
    )

    check_file_exists = BashOperator(
        task_id='check_file_exists',
        bash_command='test -f /tmp/dummy.txt'
    )

    read_file = PythonOperator(
        task_id='read_file',
        python_callable=lambda: print(open('/tmp/dummy.txt', 'rb').read())
    )

    create_file >> check_file_exists >> read_file




