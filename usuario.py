from conexao import Conexao

class Usuario():
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.email = None
        self.logado = False

    def cadastrar_motorista(self,nome, cpf, cnh, cnpj, telefone, email, senha):
        # try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"""INSERT INTO tb_motoristas (nome_motorista, cpf_motorista, cnh, cnpj, tel_motorista, email_motorista, senha_motorista)
            VALUES ('{nome}', '{cpf}', '{cnh}', '{cnpj}', '{telefone}', '{email}', '{senha}');
            """
            mycursor.execute(sql)

            mydb.commit()
            mycursor.close()

            return True
        
        # except Exception as e:

        #     print(f"Erro ao cadastrar motorista: {e}")
        #     return False

    def cadastrar_aluno(self, nome_aluno, foto_aluno, condicao_medica, escola, nome_responsavel, cpf_responsavel, endereco_responsavel, tel_responsavel, email_responsavel, senha_responsavel):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql_responsavel = """
            INSERT INTO tb_responsavel (nome_responsavel, cpf_responsavel, endereco_responsavel, tel_responsavel, email_responsavel, senha_responsavel)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values_responsavel = (nome_responsavel, cpf_responsavel, endereco_responsavel, tel_responsavel, email_responsavel, senha_responsavel)
            mycursor.execute(sql_responsavel, values_responsavel)

            sql_aluno = """
            INSERT INTO tb_alunos (nome_aluno, foto_aluno, condicao_medica, idade, responsavel_aluno)
            VALUES (%s, %s, %s, 0, %s)
            """
            values_aluno = (nome_aluno, foto_aluno, condicao_medica, cpf_responsavel)
            mycursor.execute(sql_aluno, values_aluno)

            mydb.commit()
            mycursor.close()
            return True
        except Exception as e:
            print(f"Erro ao cadastrar aluno: {e}")
            return False

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