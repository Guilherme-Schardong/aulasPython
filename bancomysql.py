import mysql.connector



conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='colegio',
)
cursor = conexao.cursor()

nome = 'Jeferson'
idade = 25
sexo = 1


# comando =f'INSERT INTO cliente (nomeCliente, idadeCliente, idSexo) VALUES ("{nome}", {idade}, {sexo})'
# cursor.execute(comando)
# conexao.commit()  # sempre que voce edita o banco de dados

# resultado = cursor.fetchall() # sempre que voce ler o banco de dados



#create
# comando =f'INSERT INTO cliente (nomeCliente, idadeCliente, idSexo) VALUES ("{nome}", {idade}, {sexo})'
# cursor.execute(comando)
# conexao.commit()  # sempre que voce edita o banco de dados



#read
# comando = 'SELECT * FROM cliente'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(resultado)

#update
# nome_novo= 'Joaquim'
# comando =f'UPDATE cliente SET nomeCliente = "{nome_novo}" WHERE idCliente = 9 '
# cursor.execute(comando)
# conexao.commit()


#delete
nome_novo= 'Joaquim'
comando =f'DELETE FROM cliente WHERE idCliente = 9 '
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()