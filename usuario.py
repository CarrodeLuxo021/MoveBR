from conexao import Conexao

class Usuario():
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.email = None
        self.logado = False

    def cadastrar_motorista(self,nome, cpf, cnh, cnpj, telefone, email, senha):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"""INSERT INTO tb_motoristas (nome_motorista, cpf_motorista, cnh, cnpj, tel_motorista, email_motorista, senha_motorista)
            VALUES ('{nome}', '{cpf}', '{cnh}', '{cnpj}', '{telefone}', '{email}', '{senha}');
            """
            mycursor.execute(sql)

            mydb.commit()
            mycursor.close()

            return True
        
        except Exception as e:

            print(f"Erro ao cadastrar motorista: {e}")
            return False

    def cadastrar_aluno(self, nome_aluno, foto_aluno, condicao_medica, escola, nome_responsavel, endereco_responsavel, tel_responsavel, email_responsavel):
        # try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"""
            INSERT INTO tb_alunos (nome_aluno, foto_aluno, condicao_medica, escola,  nome_responsavel, endereco, telefone_responsavel, email_responsavel)          
            VALUES ('{nome_aluno}', '{foto_aluno}',  '{condicao_medica}',  '{escola}',  '{nome_responsavel}',  '{endereco_responsavel}',  '{tel_responsavel}',  '{email_responsavel}');

            """
    
            mycursor.execute(sql)
            mydb.commit()
            mycursor.close()
            return True
        # except Exception as e:
        #     print(f"Erro ao cadastrar aluno: {e}")
        #     return False

    def logar(self, email, senha):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = "SELECT nome_motorista, cpf_motorista, email_motorista FROM tb_motoristas WHERE email_motorista = %s AND senha_motorista = %s"
            values = (email, senha)
            mycursor.execute(sql, values)

            resultado = mycursor.fetchone()
            if resultado:
                self.nome = resultado[0]
                self.cpf = resultado[1]
                self.email = resultado[2]
                self.logado = True
            else:
                self.logado = False

            mycursor.close()
            mydb.close()
            return self.logado
        except Exception as e:
            print(f"Erro ao logar: {e}")
            return False
        

           
        
    def listar_aluno(self):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"SELECT nome_aluno, foto_aluno, condicao_medica, escola, telefone_responsavel, nome_responsavel, endereco, id_aluno FROM tb_alunos"

            mycursor.execute(sql)
            resultados = mycursor.fetchall()
            alunos = []
            for linha in resultados:
                alunos.append({"nome_aluno":linha[0],
                               "foto_aluno": linha[1],
                               "condicao_medica": linha[2],
                               "escola": linha[3],
                               "telefone_responsavel": linha[4],
                               "nome_responsavel": linha[5],
                               "endereco": linha[6],
                               "id_aluno": linha[7]

                })
    
            mydb.close()
            return alunos
        except:
            return False
    
    def excluir_aluno(self, id_aluno):

        mydb = Conexao.conectar()
        mycursor = mydb.cursor()

        sql = f"DELETE  FROM tb_alunos WHERE id_aluno = {id_aluno}"
        mycursor.execute(sql)
        mydb.commit()
        mydb.close()
        return True
    
    def pesquisar_aluno(self, pesquisa):
        mydb = Conexao.conectar()
        mycursor = mydb.cursor()

        sql = f"SELECT  nome_aluno, foto_aluno, condicao_medica, escola, telefone_responsavel, nome_responsavel, endereco FROM tb_alunos WHERE escola = '{pesquisa}'"

        mycursor.execute(sql)
        resultados = mycursor.fetchall()
        alunosf = []

        for aluno in resultados:
            alunosf.append({
                            "nome_aluno":aluno[0],
                            "foto_aluno": aluno[1],
                            "condicao_medica": aluno[2],
                            "escola": aluno[3],
                            "telefone_responsavel": aluno[4],
                            "nome_responsavel": aluno[5],
                            "endereco": aluno[6]
            })
        mydb.close()
        return alunosf       