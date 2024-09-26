import mysql.connector

class Conexao:

    def conectar():
        mydb = mysql.connector.connect(
            user="root",
            password="root",
            host="localhost",
            database="movebr",
            port="3306"
        )
        
        return mydb