# data: 04/11/2024
# nesta primeira aula vamoa aprender os comando de conexão co o banco de dados Oracle

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
    print("-"*50)

    # Criando um cursor para executar comando SQL
    cursor = connection.cursor()

    # Exemplo de consulta
    cursor.execute("INSERT INTO TB_VENDEDORES (MATRICULA, NOME, DATA_ADMISSAO, PERCENTUAL_COMISSAO) VALUES ('00810', 'Marcia Almeida', '14/12/2016', 0.18)")
    connection.commit() # commit = entregar
    print('Inclusão realizada com sucesso!')

except cx_Oracle.DatabaseError as e:
    print(f"Erro ao conectar: {e}!")

## Erro ao conectar: ORA-00913: valores demais! = Valor duplicado ##
