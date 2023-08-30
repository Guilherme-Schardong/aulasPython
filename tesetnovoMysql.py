import mysql.connector
from mysql.connector import Error

# try:
#     con = mysql.connector.connect(
#         host='localhost',
#         database='colegio',
#         user='root',
#         password=''
#     )

#     consulta_sql = 'SELECT * FROM cliente'
#     cursor = con.cursor()
#     cursor.execute(consulta_sql)
#     linhas = cursor.fetchall()

#     print('numero de registros retornados', cursor.rowcount)
#     print('\nMostrar os clientes cadastrados')

#     for linha in linhas:
#         print('Id do cliente: ', linha[0])
#         print('Nome do cliente: ', linha[1])
#         print('Idade do cliente: ', linha[2])
#         print('Sexo do cliente: ', linha[3])
#         print('Cidade do cliente: ', linha[4])
#         print('Altura do cliente: ', linha[5], '\n')


# except Error as erro:
#     print('Falha ao acessar tabela MySQL: ', erro)

# finally:
#     if(con.is_connected()):
#         cursor.close()
#         con.close()
#         print('Conexão ao MySQL finalizada')


try:
    con = mysql.connector.connect(
        host='localhost',
        database='colegio',
        user='root',
        password=''
    )
    
    name = 'Luanel'
    idade = '1990-09-25'
    sexo = 1
    cidade = 2
    altura = 1.88
    inserir_cliente = f'''INSERT INTO cliente
                            (nomeCliente, dataNascimentoCliente, idSexo, idCidade, altura)
                            VALUES
                            ('{name}','{idade}', {sexo}, {cidade}, {altura})'''
    cursor= con.cursor()
    cursor.execute(inserir_cliente)
    con.commit()
    print(cursor.rowcount, 'registros foram inseridos')


except Error as erro:
    print('Falaha ao iserir dados MySQL: ', erro)
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print('Conexão ao MySQL finalizada')