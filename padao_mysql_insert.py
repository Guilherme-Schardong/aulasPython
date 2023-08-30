import mysql.connector
from mysql.connector import Error


def conectar():

    try:
        global con
        con = mysql.connector.connect(
        host='localhost',
        database='colegio',
        user='root',
        password=''
        )
    except Error as erro:
        print('Erro de conexão '+ erro)


try:
    # con = mysql.connector.connect(
    #     host='localhost',
    #     database='colegio',
    #     user='root',
    #     password=''
    # )
    conectar()
    nome = 'jose almeida prado'
    idade = '1990-09-25'
    sexo = 1
    cidade = 1
    altura = 1.88
    inserir_clientes = f"""INSERT INTO cliente
                            (nomeCliente, dataNascimentoCliente, idSexo, idCidade, altura)
                            VALUES
                            ("{nome}", "{idade}", {sexo},{cidade},{altura})
                        """
    cursor = con.cursor()
    cursor.execute(inserir_clientes)
    con.commit()
    print(cursor.rowcount, 'registros inseridos na tabela!')
    cursor.close()
except Error as erro:
    print('Falha ao inserir dadods MySQL: {}'.format(erro))
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print('Conexão ao MySQL finalizada')