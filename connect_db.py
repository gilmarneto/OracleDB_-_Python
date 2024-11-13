# data: 01/11/2024
# nesta primeira aula vamos aprender os comando de conexão com o banco de dados OracleDB

# primeiro vamos instalar a biblioteca "cx_Oracle"
# Mas antes instalar: "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
# pip install cx_Oracle
# após a instalação vamos importar a biblioteca
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
    
except cx_Oracle.DatabaseError as e:
    print(f"Erro ao conectar: {e}!")