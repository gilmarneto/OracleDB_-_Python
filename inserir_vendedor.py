# data: 11/11/2024
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
# Variáveis
continuar = 1 
"""
matricula = '00212'
nome_vendedor = 'Joaquim Santos'
data_admissao = '08/11/24'
percentual_comissao = 0.12
"""
try:
    # Conectando ao banco de dados
    connection = cx_Oracle.connect(user=USERNAME, password=PASSWORD, dsn=DSN)
    print("Conexão estabelecida com sucesso.")
    print("-"*50)
    print("----- Cadastro de Vendedores -----")

    # Criando um cursor para executar comando SQL
    cursor = connection.cursor()

    while continuar == 1:
        # entrada de informações
        matricula = input('Nº de matricula: ' )
        nome_vendedor = input('Nome vendedor: ')
        data_admissao = input('Data de admissão: ')
        percentual_comissao = float(input('Percentual de comissão: '))
        # Exemplo de consulta
        cursor.execute(f"INSERT INTO TB_VENDEDORES (MATRICULA, NOME, DATA_ADMISSAO, PERCENTUAL_COMISSAO) VALUES ('{matricula}', '{nome_vendedor}', TO_DATE('{data_admissao}', 'DD/MM/YYYY'), {percentual_comissao})")
        connection.commit() # commit = entregar
        print('Inclusão realizada com sucesso!')
        continuar = input('Deseja continuar com o cadastro, 1(sim), 0(não)? ')

except cx_Oracle.DatabaseError as e:
    print(f"Erro ao conectar: {e}!")

## Erro ao conectar: ORA-00913: valores demais! = Valor duplicado ##