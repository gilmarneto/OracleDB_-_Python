## data: 13/11/24

## vamos aprender abrir aruivos (.csv), pegar seus valores linha à linha e inserir no banco de dados

import cx_Oracle, os, csv

# Exemplo
# with open('nome_arquivo.csv', 'r'(leitura)) as csvfile:
    # reader = csv.reader(csvfile)
    # for row(linha) in reader:
        #print(row)

# configurações de conexão
USERNAME = 'system'
PASSWORD = '123'
# Data Source Name, usado para definir a localização do banco de dados. Pode ser no formato (host: porta/banco
DSN = 'localhost:1521/xe' # Exemplo de DSN(Data Source Name)
# limpar saída
os.system('cls')
# abrir arquivo csv, capturar valores e salvar no banco de dados        
with open('clientes.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # desconsidera a linha de título
    try:
        # Conectando ao banco de dados
        connection = cx_Oracle.connect(user=USERNAME, password=PASSWORD, dsn=DSN)
        print("Conexão estabelecida com sucesso.")
        # Criando um cursor para executar comando SQL
        cursor = connection.cursor()
        # pegar linha à linha do arquivo CSV
        for linha in reader: 
            cursor.execute(f"INSERT INTO TB_CLIENTES (CPF, NOME, ENDERECO1, ENDERECO2, BAIRRO, CIDADE, ESTADO, CEP, DATA_NASCIMENTO, SEXO, LIMITE_CREDITO, VOLUME_COMPRA, PRIMEIRA_COMPRA) VALUES ('{linha[0]}', '{linha[1]}', '{linha[2]}', '{linha[3]}', '{linha[4]}', '{linha[5]}', '{linha[6]}', '{linha[7]}', '{linha[8]}', '{linha[9]}', {int(linha[10])}, {int(linha[11])}, {int(linha[12])})")
            connection.commit() # commit = entregar
            print('Inclusão realizada com sucesso!')
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao conectar: {e}!!")