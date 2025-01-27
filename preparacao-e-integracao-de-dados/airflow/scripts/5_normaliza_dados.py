# Bibliotecas
import pandas as pd
import os

# Leitura dos arquivos CSV
dados_alunos_df = pd.read_csv('/usr/local/datasets/trabalho/raw/dados_alunos.csv')
grade_curricular_df = pd.read_csv('/usr/local/datasets/trabalho/raw/grade_curricular.csv')

# Ajuste do esquema das colunas de data
dados_alunos_df['nascimento'] = pd.to_datetime(dados_alunos_df['nascimento'], dayfirst=True)
dados_alunos_df['ingresso'] = pd.to_datetime(dados_alunos_df['ingresso'], dayfirst=True)
dados_alunos_df['conclusao_prevista'] = pd.to_datetime(dados_alunos_df['conclusao_prevista'], dayfirst=True)
dados_alunos_df['conclusao'] = pd.to_datetime(dados_alunos_df['conclusao'], dayfirst=True)

# Ajuste do formato do telefone para o padrão "+55 XX XXXXX-XXXX"
dados_alunos_df['telefone'] = dados_alunos_df['telefone'].apply(lambda x: f"+55 {str(x)[2:4]} {str(x)[4:9]}-{str(x)[9:]}")

# Primeira Forma Normal (1FN): Eliminar grupos repetitivos e garantir que todos os atributos contenham valores atômicos
# A tabela 'dados_alunos_df' já está na 1FN, pois todas as colunas contêm valores atômicos.

# Segunda Forma Normal (2FN): Garantir que todos os atributos não-chave sejam totalmente dependentes da chave primária
# Criar a tabela `Alunos` separando os dados dos alunos, garantindo que cada aluno seja identificado unicamente pelo CPF (cadastro).
alunos_df = dados_alunos_df[['cadastro', 'nome', 'nascimento', 'sexo', 'email', 'endereco', 'telefone']].drop_duplicates()

# Criar a tabela `Matrículas` para representar as matrículas de cada aluno em cursos específicos.
matriculas_df = dados_alunos_df[['matricula', 'cadastro', 'cod_curso', 'ingresso', 'conclusao_prevista', 'conclusao', 'status']]

# Terceira Forma Normal (3FN): Eliminar dependências transitivas
# Criar a tabela `Cursos` para representar os cursos oferecidos, garantindo que não haja dependências transitivas.
cursos_df = grade_curricular_df[['cod_curso', 'curso', 'periodos']].drop_duplicates()

# Criar a tabela `Disciplinas` para representar as disciplinas, separando-as dos dados dos cursos.
disciplinas_df = grade_curricular_df[['cod_disciplina', 'nome_disciplina', 'tipo', 'nota_de_corte', 'carga_horária_prevista', 'frequência_mínima']].drop_duplicates()

# Criar a tabela `GradeCurricular` para mapear quais disciplinas pertencem a quais cursos e períodos.
grade_curricular_normalizada_df = grade_curricular_df[['cod_curso', 'periodo', 'cod_disciplina']]

# Diretório de saída para os arquivos CSV normalizados
output_dir = '/usr/local/datasets/trabalho/consume/'

# Certificar-se de que o diretório existe
os.makedirs(os.path.dirname(output_dir), exist_ok=True)

# Salvar as tabelas normalizadas em formato CSV
alunos_df.to_csv(os.path.join(output_dir, "Alunos.csv"), index=False)
matriculas_df.to_csv(os.path.join(output_dir, "Matriculas.csv"), index=False)
cursos_df.to_csv(os.path.join(output_dir, "Cursos.csv"), index=False)
disciplinas_df.to_csv(os.path.join(output_dir, "Disciplinas.csv"), index=False)
grade_curricular_normalizada_df.to_csv(os.path.join(output_dir, "GradeCurricular.csv"), index=False)
