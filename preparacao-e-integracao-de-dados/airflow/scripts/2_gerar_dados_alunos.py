# Bibliotecas
import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta, date
import os

# Inicializa o Faker com a localidade brasileira
fake = Faker('pt_BR')

# Garante que os dados gerados sejam reproduzíveis
fake.seed_instance(0)

# Função para carregar os dados do arquivo grade_curricular.csv
def carregar_dados_cursos(arquivo_csv):
    df = pd.read_csv(arquivo_csv)
    cursos = df[['cod_curso', 'curso']].drop_duplicates().set_index('cod_curso')['curso'].to_dict()
    periodos = df.groupby('cod_curso')['periodo'].max().to_dict()
    return cursos, periodos

# Carrega os dados dos cursos a partir do arquivo CSV
cursos_csv = '/usr/local/datasets/trabalho/raw/grade_curricular.csv'
cursos_dict, periodos_dict = carregar_dados_cursos(cursos_csv)

# Adiciona a média de alunos por curso
media_alunos = {
    'ENGENHARIA DE COMPUTAÇÃO': 50,
    'CIÊNCIA DA COMPUTAÇÃO': 62,
    'SISTEMA DE INFORMAÇÕES': 48,
    'JOGOS DIGITAIS': 32,
    'TECNÓLOGO EM REDES DIGITAIS': 28
}

# Combina os dados de cursos e períodos em um único dicionário
cursos = {cod: {'nome': nome, 'media_alunos': media_alunos[nome], 'periodos': periodos_dict[cod]} for cod, nome in cursos_dict.items()}

# Função para determinar a data de conclusão prevista
def calcular_conclusao_prevista(ingresso, periodos):
    ingresso_date = datetime.strptime(ingresso, '%d/%m/%Y')
    conclusao_date = ingresso_date + timedelta(days=periodos * 6 * 30)  # 6 meses por período
    return conclusao_date.strftime('%d/%m/%Y')

# Função geradora dos dados dos alunos
def gerar_dados_alunos(num_alunos, cursos):
    alunos = []
    # Define o intervalo de datas para ingresso
    start_date = date(2015, 1, 1)
    end_date = datetime.today().date()
    
    for _ in range(num_alunos):
        # Gera número de matrícula único
        matricula = fake.unique.random_int(min=100000, max=999999)
        
        # Seleciona sexo aleatoriamente
        sexo = random.choice(['M', 'F'])
        
        # Gera nome baseado no sexo
        if sexo == 'M':
            nome = fake.first_name_male() + ' ' + fake.last_name()
        else:
            nome = fake.first_name_female() + ' ' + fake.last_name()
        
        # Gera CPF único
        cadastro = fake.unique.cpf()
        
        # Gera data de nascimento
        nascimento = fake.date_of_birth(minimum_age=18).strftime('%d/%m/%Y')
        
        # Gera email baseado no nome
        email = f'{nome.lower().replace(" ", ".")}@trabalhopuc.br'
        
        # Gera endereço aleatório
        endereco = f'{fake.city()}, {fake.estado_sigla()}'
        
        # Gera número de telefone
        telefone = fake.msisdn()
        
        # Seleciona curso aleatoriamente
        curso = random.choice(list(cursos.keys()))
        
        # Gera data de ingresso entre 2015 e hoje, apenas em 1º de janeiro ou 1º de julho
        ingresso_date = fake.date_between_dates(date_start=start_date, date_end=end_date)
        if ingresso_date.day == 1 and (ingresso_date.month == 1 or ingresso_date.month == 7):
            ingresso = ingresso_date.strftime('%d/%m/%Y')
        else:
            ingresso = random.choice([date(ingresso_date.year, 1, 1), date(ingresso_date.year, 7, 1)]).strftime('%d/%m/%Y')
        
        # Calcula a data prevista de conclusão
        conclusao_prevista = calcular_conclusao_prevista(ingresso, cursos[curso]['periodos'])
        
        # Define status da matrícula
        status = random.choice(['Ativo', 'Trancado', 'Cancelado', 'Concluido'])
        
        # Define conclusão real dependendo do status
        if status == 'Ativo' or status == 'Trancado':
            conclusao = None
        elif status == 'Concluido':
            # Conclusão em 30 de junho ou 31 de dezembro
            conclusao = random.choice([date(end_date.year, 6, 30), date(end_date.year, 12, 31)])
            if conclusao > end_date:
                conclusao -= timedelta(days=365)  # Ajustar para o ano anterior se estiver no futuro
            conclusao = conclusao.strftime('%d/%m/%Y')
        elif status == 'Cancelado':
            conclusao = fake.date_between_dates(date_start=ingresso_date, date_end=end_date).strftime('%d/%m/%Y')
            conclusao_prevista = None
        
        # Adiciona os dados do aluno à lista
        alunos.append([matricula, nome, cadastro, nascimento, sexo, email, endereco, telefone, curso, ingresso, conclusao_prevista, conclusao, status])
    
    return alunos

# Lista de códigos dos cursos disponíveis
cod_cursos = list(cursos.keys())

# Define o número de alunos a serem gerados
num_alunos = sum(curso['media_alunos'] for curso in cursos.values())  # Média de alunos por curso

# Gera os dados dos alunos
dados_alunos = gerar_dados_alunos(num_alunos, cursos)

# Define as colunas do DataFrame
colunas = ['matricula', 'nome', 'cadastro', 'nascimento', 'sexo', 'email', 'endereco', 'telefone', 'cod_curso', 'ingresso', 'conclusao_prevista', 'conclusao', 'status']

# Cria o DataFrame com os dados dos alunos
df_alunos = pd.DataFrame(dados_alunos, columns=colunas)

# Salva o DataFrame em um arquivo CSV
arquivo_csv_alunos = '/usr/local/datasets/trabalho/raw/dados_alunos.csv'

# Certificar-se de que o diretório existe
os.makedirs(os.path.dirname(arquivo_csv_alunos), exist_ok=True)

# Salvar para um arquivo CSV
df_alunos.to_csv(arquivo_csv_alunos, index=False)
