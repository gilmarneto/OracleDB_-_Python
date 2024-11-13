# data: 06/11/2024
# nesta aula vamos aprender a atualizar dados de uma tabela

# vamos importar a biblioteca
import cx_Oracle
# limpar saída
import os
os.system('cls')
# configurações de conexão
USERNAME = 'system'
PASSWORD = '123'
# Data Source Name, usado para definir a localização do banco de dados. Pode ser no formato (host: porta/banco
DSN = 'localhost:1521/xe' # Exemplo de DSN(Data Source Name)
# Minhas variáveis
continuar = 1

try:
    # Conectando ao banco de dados
    connection = cx_Oracle.connect(user=USERNAME, password=PASSWORD, dsn=DSN)
    print("Conexão estabelecida com sucesso.")
    print("-"*50)
    print("----- Atualização -----")
    # Criando um cursor para executar comando SQL
    cursor = connection.cursor()

    while continuar == 1:
        matricula = input('Informe o número de matricula: ')
        comissao = float(input('Informe o novo percentual de comissão: '))
        # Exemplo de atualização
        cursor.execute(f"UPDATE TB_VENDEDORES SET PERCENTUAL_COMISSAO = {comissao} WHERE MATRICULA = {matricula}")
        connection.commit()
        print('Dados atualizados com sucesso.')
        continuar = int(input('Deseja continuar atualizando os dados, 1 para "sim" e 0 para "não"? '))

except cx_Oracle.DatabaseError as e:
    print(f"Erro ao conectar: {e}!")