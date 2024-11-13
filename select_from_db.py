# data: 01/11/2024
# nesta aula vamos aprender o comando SELECT

# importar a biblioteca
import cx_Oracle
# limpar saída
import os
os.system('cls')
# configurações de conexão
USERNAME = 'system'
PASSWORD = '123'
# Data Source Name, usado para definir a localização do banco de dados. Pode ser no formato (host: porta/banco
DSN = 'localhost:1521/xe' # Exemplo de DSN(Data Source Name)

try:
    # Conectando ao banco de dados
    connection = cx_Oracle.connect(user=USERNAME, password=PASSWORD, dsn=DSN)
    print("Conexão estabelecida com sucesso.")
    print("-"*50)
    print("----- Seleção -----")

    # Criando um cursor para executar comando SQL
    cursor = connection.cursor()

    # Exemplo de consulta
    cursor.execute("SELECT * FROM TB_PRODUTOS")

    # Mostrando os resultados
    r = 0
    for row in cursor:
        print(f'{r} ----- {row}')
        r+=1
except cx_Oracle.DatabaseError as e:
    print(f"Erro ao conectar: {e}!")



