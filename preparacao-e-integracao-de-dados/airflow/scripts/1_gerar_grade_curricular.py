# Bibliotecas
import pandas as pd
import random
import os

# Dados dos cursos
cursos = {
    1: {
        'nome': 'ENGENHARIA DE COMPUTAÇÃO',
        'periodos': 10,
        'disciplinas_por_periodo': 8,
        'grade': [
            ["Cálculo I", "Física I", "Álgebra Linear", "Introdução à Computação", "Programação I", "Química Geral", "Desenho Técnico", "Inglês Técnico"],
            ["Cálculo II", "Física II", "Estruturas de Dados", "Programação II", "Circuitos Elétricos", "Eletrônica I", "Álgebra Discreta", "Metodologia Científica"],
            ["Cálculo III", "Física III", "Sistemas Digitais", "Programação III", "Teoria dos Grafos", "Eletrônica II", "Probabilidade e Estatística", "Redes de Computadores I"],
            ["Cálculo IV", "Física IV", "Banco de Dados I", "Arquitetura de Computadores", "Programação Orientada a Objetos", "Sistemas Operacionais I", "Microcontroladores", "Redes de Computadores II"],
            ["Métodos Numéricos", "Análise de Sistemas", "Banco de Dados II", "Programação Web", "Sistemas Operacionais II", "Controle e Automação", "Sinais e Sistemas", "Economia e Gestão"],
            ["Cálculo Numérico", "Inteligência Artificial I", "Engenharia de Software I", "Sistemas Embarcados", "Processamento Digital de Sinais", "Computação Gráfica", "Redes de Sensores", "Projeto Integrador I"],
            ["Inteligência Artificial II", "Engenharia de Software II", "Sistemas Distribuídos", "Projeto de Redes de Computadores", "Robótica", "Computação de Alto Desempenho", "Segurança da Informação", "Projeto Integrador II"],
            ["Tópicos Especiais em Computação", "Engenharia de Software III", "Sistemas de Controle", "Internet das Coisas", "Computação Móvel", "Automação Industrial", "Ética e Legislação em Informática", "Projeto Integrador III"],
            ["Projeto de Sistemas Embarcados", "Computação em Nuvem", "Machine Learning", "Bioinformática", "Realidade Virtual e Aumentada", "Gestão de Projetos", "Trabalho de Conclusão de Curso I", "Estágio Supervisionado I"],
            ["Visão Computacional", "Sistemas Inteligentes", "Segurança em Sistemas Embarcados", "Blockchain e Criptomoedas", "Gestão de Tecnologia da Informação", "Empreendedorismo", "Trabalho de Conclusão de Curso II", "Estágio Supervisionado II"],
        ]
    },
    2: {
        'nome': 'CIÊNCIA DA COMPUTAÇÃO',
        'periodos': 8,
        'disciplinas_por_periodo': 8,
        'grade': [
            ["Cálculo I", "Física I", "Introdução à Computação", "Programação I", "Álgebra Linear", "Comunicação e Expressão", "Inglês Técnico", "Metodologia Científica"],
            ["Cálculo II", "Física II", "Estruturas de Dados", "Programação II", "Álgebra Discreta", "Arquitetura de Computadores", "Probabilidade e Estatística", "Ética e Legislação em Informática"],
            ["Cálculo III", "Física III", "Banco de Dados I", "Programação Orientada a Objetos", "Teoria dos Grafos", "Sistemas Operacionais I", "Redes de Computadores I", "Linguagens Formais e Autômatos"],
            ["Matemática Discreta", "Física IV", "Banco de Dados II", "Sistemas Operacionais II", "Redes de Computadores II", "Engenharia de Software I", "Métodos Numéricos", "Economia e Gestão"],
            ["Inteligência Artificial I", "Engenharia de Software II", "Programação Web", "Processamento de Imagens", "Computação Gráfica", "Sistemas Distribuídos", "Segurança da Informação", "Análise de Sistemas"],
            ["Inteligência Artificial II", "Engenharia de Software III", "Computação Móvel", "Sistemas Embarcados", "Tópicos Especiais em Computação", "Gestão de Projetos", "Trabalho de Conclusão de Curso I", "Estágio Supervisionado I"],
            ["Aprendizado de Máquina", "Bioinformática", "Computação em Nuvem", "Robótica", "Realidade Virtual e Aumentada", "Visão Computacional", "Trabalho de Conclusão de Curso II", "Estágio Supervisionado II"],
            ["Projeto de Redes de Computadores", "Segurança de Redes", "Gestão de Tecnologia da Informação", "Computação de Alto Desempenho", "Blockchain e Criptomoedas", "Sistemas Inteligentes", "Empreendedorismo", "Inovação Tecnológica"],
        ]
    },
    3: {
        'nome': 'SISTEMA DE INFORMAÇÕES',
        'periodos': 8,
        'disciplinas_por_periodo': 7,
        'grade': [
            ["Cálculo I", "Introdução à Computação", "Programação I", "Álgebra Linear", "Comunicação e Expressão", "Inglês Técnico", "Metodologia Científica"],
            ["Cálculo II", "Estruturas de Dados", "Programação II", "Álgebra Discreta", "Arquitetura de Computadores", "Probabilidade e Estatística", "Ética e Legislação em Informática"],
            ["Matemática Discreta", "Banco de Dados I", "Programação Orientada a Objetos", "Teoria dos Grafos", "Sistemas Operacionais I", "Redes de Computadores I", "Linguagens Formais e Autômatos"],
            ["Banco de Dados II", "Sistemas Operacionais II", "Redes de Computadores II", "Engenharia de Software I", "Métodos Numéricos", "Economia e Gestão", "Análise de Sistemas"],
            ["Inteligência Artificial I", "Engenharia de Software II", "Programação Web", "Processamento de Imagens", "Computação Gráfica", "Sistemas Distribuídos", "Segurança da Informação"],
            ["Inteligência Artificial II", "Engenharia de Software III", "Computação Móvel", "Sistemas Embarcados", "Tópicos Especiais em Computação", "Gestão de Projetos", "Trabalho de Conclusão de Curso I"],
            ["Aprendizado de Máquina", "Bioinformática", "Computação em Nuvem", "Robótica", "Realidade Virtual e Aumentada", "Trabalho de Conclusão de Curso II", "Estágio Supervisionado I"],
            ["Projeto de Redes de Computadores", "Segurança de Redes", "Gestão de Tecnologia da Informação", "Computação de Alto Desempenho", "Blockchain e Criptomoedas", "Empreendedorismo", "Inovação Tecnológica"],
        ]
    },
    4: {
        'nome': 'JOGOS DIGITAIS',
        'periodos': 6,
        'disciplinas_por_periodo': 6,
        'grade': [
            ["Introdução aos Jogos Digitais", "Programação I", "Desenho e Animação", "Álgebra Linear", "Comunicação e Expressão", "Inglês Técnico"],
            ["Programação II", "Design de Jogos", "Estruturas de Dados", "Matemática Discreta", "Física para Jogos", "Modelagem 3D"],
            ["Programação Orientada a Objetos", "Inteligência Artificial para Jogos", "Banco de Dados", "Redes de Computadores", "Roteirização e Narrativas Interativas", "Computação Gráfica"],
            ["Programação de Jogos", "Design de Níveis", "Engenharia de Software", "Interfaces Homem-Máquina", "Áudio para Jogos", "Teste e Depuração de Jogos"],
            ["Realidade Virtual e Aumentada", "Projeto de Jogos Digitais", "Desenvolvimento de Jogos para Dispositivos Móveis", "Análise e Modelagem de Requisitos", "Gestão de Projetos de Jogos", "Economia e Gestão"],
            ["Tópicos Especiais em Jogos Digitais", "Empreendedorismo", "Ética e Legislação em Jogos Digitais", "Inovação Tecnológica", "Trabalho de Conclusão de Curso", "Estágio Supervisionado"],
        ]
    },
    5: {
        'nome': 'TECNÓLOGO EM REDES DIGITAIS',
        'periodos': 4,
        'disciplinas_por_periodo': 6,
        'grade': [
            ["Introdução às Redes de Computadores", "Programação I", "Arquitetura de Computadores", "Sistemas Operacionais", "Inglês Técnico", "Metodologia Científica"],
            ["Redes de Computadores I", "Programação II", "Segurança de Redes", "Administração de Sistemas", "Redes Sem Fio", "Comunicação e Expressão"],
            ["Redes de Computadores II", "Programação para Redes", "Gerenciamento de Redes", "Protocolos de Redes", "Segurança da Informação", "Economia e Gestão"],
            ["Computação em Nuvem", "Infraestrutura de TI", "Tópicos Especiais em Redes Digitais", "Gestão de Projetos de TI", "Trabalho de Conclusão de Curso", "Estágio Supervisionado"],
        ]
    }
}

# Dicionário para armazenar os códigos de disciplinas
codigos_disciplinas = {}
codigo_atual = 1

# Função para determinar o tipo de disciplina
def determinar_tipo_disciplina(nome_disciplina):
    disciplinas_praticas = [
        "Programação I", "Programação II", "Programação III", "Programação Web", 
        "Programação de Jogos", "Programação Orientada a Objetos", "Redes de Computadores I",
        "Redes de Computadores II", "Desenho Técnico", "Desenho e Animação",
        "Modelagem 3D", "Sistemas Operacionais", "Projeto Integrador I",
        "Projeto Integrador II", "Projeto Integrador III", "Teste e Depuração de Jogos",
        "Projeto de Jogos Digitais", "Desenvolvimento de Jogos para Dispositivos Móveis",
        "Trabalho de Conclusão de Curso I", "Trabalho de Conclusão de Curso II",
        "Estágio Supervisionado I", "Estágio Supervisionado II"
    ]
    return "Prática" if nome_disciplina in disciplinas_praticas else "Teórica"

# Função para calcular a frequência mínima
def calcular_frequencia_minima(carga_horaria):
    return int(carga_horaria * 0.75)

# Lista para armazenar os dados
dados = []

# Gerar as linhas com as informações solicitadas
for cod_curso, curso_info in cursos.items():
    curso_nome = curso_info['nome']
    total_periodos = curso_info['periodos']
    for periodo in range(1, total_periodos + 1):
        disciplinas = curso_info['grade'][periodo - 1]
        for nome_disciplina in disciplinas:
            if nome_disciplina not in codigos_disciplinas:
                codigos_disciplinas[nome_disciplina] = codigo_atual
                codigo_atual += 1
            cod_disciplina = codigos_disciplinas[nome_disciplina]
            tipo_disciplina = determinar_tipo_disciplina(nome_disciplina)
            carga_horaria_prevista = random.randint(17, 47)
            frequencia_minima = calcular_frequencia_minima(carga_horaria_prevista)
            dados.append([cod_curso, curso_nome, periodo, total_periodos, cod_disciplina, nome_disciplina, tipo_disciplina, 70, carga_horaria_prevista, frequencia_minima])

# Criar o DataFrame
df = pd.DataFrame(dados, columns=['cod_curso', 'curso', 'periodo', 'periodos', 'cod_disciplina', 'nome_disciplina', 'tipo', 'nota_de_corte', 'carga_horária_prevista', 'frequência_mínima'])

# Caminho para salvar o arquivo
arquivo_csv = '/usr/local/datasets/trabalho/raw/grade_curricular.csv'

# Certificar-se de que o diretório existe
os.makedirs(os.path.dirname(arquivo_csv), exist_ok=True)

# Salvar para um arquivo CSV
df.to_csv(arquivo_csv, index=False)