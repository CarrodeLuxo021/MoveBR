import mysql.connector

class Conexao():
    def conectar():
        mydb = mysql.connector.connect(
            host="bdmovebr.mysql.database.azure.com",
            port="3306",
            user="movebr",
            password="123456789",
            database="movebr"
            )

        return mydb