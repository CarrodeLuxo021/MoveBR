import mysql.connector

class Conexao():
    def conectar():
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="movebr",
            password="123456789",
            database="movebr"
            )

        return mydb