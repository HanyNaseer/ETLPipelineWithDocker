from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import load_data  # This assumes load_data.py is in the same directory as your DAG

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 24),
    'retries': 1,
}

dag = DAG(
    'online_retail_etl',
    default_args=default_args,
    description='ETL process for Online Retail Dataset',
    schedule_interval='@daily',
)

load_data_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data.main,  # Ensure load_data.py has a main function
    dag=dag,
)

load_data_task
