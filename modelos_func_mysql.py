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