import pymysql

#Configuração do BD - CONSTANTES
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'senai'
DB_DATABASE = 'todolist'

#Função para conectar o DataBase
def conectar_db():
    conexao = pymysql.connect( #alterado aqui para outra biblioteca mysql
        host = DB_HOST,
        user= DB_USER,
        password = DB_PASSWORD,
        database = DB_DATABASE,
        cursorclass = pymysql.cursors.DictCursor #alterado aqui para outra biblioteca mysql
    )
    cursor = conexao.cursor() #alterado aqui para outra biblioteca mysql
    return conexao, cursor

#Função para encerrar o BD
def encerrar_db(cursor, conexao):
    cursor.close()
    conexao.close()