# IMPORTAÇÃO DAS BIBLIOTECAS
from azure.storage.blob import BlobClient
import os

# VARIÁVEIS DE APOIO
cadeia_conexao = ''
caminho_local = '/usr/local/datasets/trabalho/consume/'
arquivos = ['Alunos.csv', 'Cursos.csv', 'Disciplinas.csv', 'GradeCurricular.csv', 'Matriculas.csv']
container_name = 'datalake-dados-faculdade'

# MÉTODO PARA FAZER UPLOAD DE ARQUIVOS
for arquivo in arquivos:
    caminho_blob = f'consume/{arquivo.lower()}'
    blob = BlobClient.from_connection_string(conn_str=cadeia_conexao, container_name=container_name, blob_name=caminho_blob)
    with open(os.path.join(caminho_local, arquivo), "rb") as data:
        blob.upload_blob(data, overwrite=True)
