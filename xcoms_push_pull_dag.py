import uuid
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

def _generate_uuid(**context):
    model_id  = str(uuid.uuid4())
    context["task_instance"].xcom_push(key="model_id", value=model_id)
    
def _print_uuid(**context):
    model_id = context["task_instance"].xcom_pull(task_ids="generate_uuid", key="model_id")
    print(f"UUID: {model_id}")

with DAG("xcoms_push_pull_dag",
         start_date = datetime(2024, 5, 1),
         schedule = None):
    
    generate_uuid = PythonOperator(task_id="generate_uuid", python_callable=_generate_uuid)

    print_uuid = PythonOperator(task_id="print_uuid", python_callable=_print_uuid)

    generate_uuid >> print_uuid
