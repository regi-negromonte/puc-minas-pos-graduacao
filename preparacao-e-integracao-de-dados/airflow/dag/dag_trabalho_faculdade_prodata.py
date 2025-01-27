from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now(),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=60),
}

dag = DAG(
    'DAG_FACULDADE_PRODATA',
    default_args=default_args,
    description='DAG Trabalho - Prep. e Int. de Dados',
    schedule_interval='*/50 * * * *',
)

# Task para gerar a grade curricular
gerar_grade_curricular_raw = BashOperator(
    task_id='gerar_grade_curricular_raw',
    bash_command='python3 /usr/local/airflow/scripts/1_gerar_grade_curricular.py',
    dag=dag,
)

# Task para gerar dados dos alunos
gerar_dados_alunos_raw = BashOperator(
    task_id='gerar_dados_alunos_raw',
    bash_command='python3 /usr/local/airflow/scripts/2_gerar_dados_alunos.py',
    dag=dag,
)

# Task para carregar dados na camada raw
carregar_dados_camada_raw = BashOperator(
    task_id='carregar_dados_camada_raw',
    bash_command='python3 /usr/local/airflow/scripts/3_carregar_dados_camada_raw.py',
    dag=dag,
)

# Task para normalizar os dados
normalizar_dados = BashOperator(
    task_id='normalizar_dados',
    bash_command='python3 /usr/local/airflow/scripts/5_normaliza_dados.py',
    dag=dag,
)

# Task para carregar dados na consume zone
carregar_dados_consume_zone = BashOperator(
    task_id='carregar_dados_consume_zone',
    bash_command='python3 /usr/local/airflow/scripts/6_carregar_dados_consume_zone.py',
    dag=dag,
)

gerar_grade_curricular_raw >> gerar_dados_alunos_raw >> carregar_dados_camada_raw
gerar_grade_curricular_raw >> gerar_dados_alunos_raw >> normalizar_dados >> carregar_dados_consume_zone