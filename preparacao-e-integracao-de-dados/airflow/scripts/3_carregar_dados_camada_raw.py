# BIBLIOTECAS
from azure.storage.blob import BlobClient

# VARIAVEIS DE APOIO
dados_alunos = '/usr/local/datasets/trabalho/raw/dados_alunos.csv'
dados_grade = '/usr/local/datasets/trabalho/raw/grade_curricular.csv'
cadeia_conexao = 'DefaultEndpointsProtocol=https;AccountName=xxxxxxxxxxxxxx;AccountKey=xxxxxxxxxxxxxxxxxxxxxx'

# METODO PARA FAZER UPLOAD DE ARQUIVOS
arquivo_dados_alunos = 'raw/dados_alunos/dados_alunos.csv'
blob = BlobClient.from_connection_string(conn_str=cadeia_conexao, container_name="datalake-dados-faculdade", blob_name=arquivo_dados_alunos)
with open(dados_alunos, "rb") as data:
  blob.upload_blob(data, overwrite = True)

arquivo_dados_grade = 'raw/dados_grade/grade_curricular.csv'
blob = BlobClient.from_connection_string(conn_str=cadeia_conexao, container_name="datalake-dados-faculdade", blob_name=arquivo_dados_grade)
with open(dados_grade, "rb") as data:
  blob.upload_blob(data, overwrite = True)