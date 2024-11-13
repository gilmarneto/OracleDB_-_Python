
    # Exemplo de consulta
    cursor.execute("INSERT INTO TB_VENDEDORES (MATRICULA, NOME_VENDEDOR, DATA_ADMISSAO, PERCENTUAL_COMISSAO) VALUES ('00212', 'Joaquim Santos', '08/11/2024', 0.12)")
    connection.commit() # commit = entregar