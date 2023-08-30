import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(
        host='localhost',
        database='colegio',
        user='root',
        password=''
    )
    
    consulta_sql = "SELECT * FROM cliente"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()

    print('Numerdo de registros retornados: ', cursor.rowcount)

    print('\nMostrar os clientes cadastrados')
    for linha in linhas:
        print('Id do cliente: ',linha[0])
        print('Nome do cliente: ',linha[1])
        print('Idade do cliente: ',linha[2])
        print('Sexo do cliente: ',linha[3])
        print('Cidade do cliente: ',linha[4])
        print('Altura do cliente: ',linha[5], '\n')


except Error as erro:
    print('Falha ao acessar tabela MySQL: {}'.format(erro))
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print('Conexão ao MySQL finalizada')