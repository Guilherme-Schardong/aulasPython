import mysql.connector
from mysql.connector import Error


try:
    con = mysql.connector.connect(
        host='localhost',
        database='colegio',
        user='root',
        password=''
    )
    
    nome_novo = 'Joel'

    atualizacao_cliente = f'''UPDATE cliente SET nomeCliente = '{nome_novo}'
                            WHERE idCliente = 17 '''
    cursor = con.cursor()
    cursor.execute(atualizacao_cliente)
    con.commit()

    print('nome alterado com sucesso!')



except Error as erro:
    print('Falha ao acessar tabela MySQL: {}'.format(erro))
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print('Conexão ao MySQL finalizada')