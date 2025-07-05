import os
import sys
from datetime import datetime, timedelta
from pendulum import timezone


# 🔧 Ajouter le chemin du dossier etl à sys.path
etl_path = "/mnt/c/Users/1040 G6/Desktop/project/weather-tourism-project/etl"
if etl_path not in sys.path:
    sys.path.insert(0, etl_path)

#  Imports Airflow 3.x
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.timetables.trigger import CronTriggerTimetable  #  Nouveau import Airflow 3.x

#  Imports personnalisés
from extract import fetch_weather
from transform import transform_weather_data
from load import load_weather_data

# 🔧 Paramètres par défaut
default_args = {
    'owner': 'hiratra',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

#  Définition du DAG avec timetable Airflow 3.x
with DAG(
    dag_id='weather_pipeline',
    description='Pipeline météo-tourisme quotidien',
    start_date=datetime(2025, 7, 5),
    timetable=CronTriggerTimetable("0 0 * * *", timezone=timezone("UTC")),
    default_args=default_args,
    catchup=False,
    tags=['weather', 'tourism', 'etl']
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=fetch_weather
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform_weather_data
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load_weather_data
    )

    extract_task >> transform_task >> load_task
