from datetime import datetime
from airflow import DAG
from airflow.models import BaseOperator
# from airflow.providers.google.cloud.operators.gcs import GCSFileTransformOperator
# from airflow.providers.google.cloud.operators.gcs import GCSListObjectsOperator
from airflow.providers.google.cloud.operators.gcs import GCSToLocalFilesystemOperator
gcs_path_bucket = ''


with DAG('load_data_from_GCS', description='Loads data from GCS',
          schedule_interval='0 12 * * *',
          start_date=datetime(2022, 1, 1), catchup=False) as dag:
    # files_list = GCSFileTransformOperator(
    #     task_id='GCS_Files',
    #     bucket = 'resources_data_eng_app04',
    #     delimeter = '.csv',
    #     gcp_conn_id = ''
    # )
    download_file = GCSToLocalFilesystemOperator(
        task_id="download_file",
        object_name='all_data.csv',
        bucket='practice-bucket-luis',
        filename='/Users/luis.morales/Desktop',
        gcp_conn_id = 'https://storage.googleapis.com/practice-bucket-luis/all_data.csv'
    )




