## data: 13/11/24

## vamos aprender abrir aruivos (.csv), e pegar seus valores linha à linha

import os, csv

# Exemplo
# with open('nome_arquivo.csv', 'r'(leitura)) as csvfile:
    # reader = csv.reader(csvfile)
    # for row(linha) in reader:
        #print(row)

os.system('cls')        
with open('clientes.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    #next(reader) # desconsidera a linha de título
    for linha in reader:
        print(linha)