from conexao import Conexao

class Usuario():
    def __init__(self) -> None:
        pass
    def listar_usuario():
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"SELECT  FROM tb_alunos"

            mycursor.execute(sql)
            mycursor.fetchall()
            resultados = mycursor.fetchall()
            alunos = []
            for linha in resultados:
                alunos.append({"id_aluno":linha[0],
                               })
                for dados in linha:
                    print(dados)
                    mycursor.close()
                    mydb.close()
            return True
        except:
            return False
