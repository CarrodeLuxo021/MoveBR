from conexao import Conexao

class Usuario():
    def __init__(self):
        self.nome = None
        self.email = None
        self.senha = None
        self.telefone = None
        self.endereco = None
        self.cpf = None
        self.logado = False

    def cadastrar_responsaveis(nome_responsavel, endereco_responsavel, tel_responsavel, cpf_responsavel, email_responsavel, senha_responsavel):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()
                # Instrução SQL corrigida para a tabela tb_responsavel
            sql = """
            INSERT INTO tb_responsavel (nome_responsavel, endereco_responsavel, tel_responsavel, cpf_responsavel, email_responsavel, senha_responsavel)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (nome_responsavel, endereco_responsavel, tel_responsavel, cpf_responsavel, email_responsavel, senha_responsavel)

            # Executar a instrução SQL e fazer commit
            mycursor.execute(sql, valores)  

            self.nome = nome_responsavel
            self.cpf = cpf_responsavel
            self.endereco = endereco_responsavel
            self.tel = tel_responsavel
            self.email = email_responsavel
            self.senha = senha_responsavel

            
            mydb.commit()
            mydb.close()
            return True
        except:
            return False
    
    def cadastrar_motorista(self, nome, endereco, cidade, cpf, cnh, cnpj, telefone, email, senha):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()
            
            sql = """
            INSERT INTO tb_motoristas (nome, cpf, cnh, cnpj, cidade, endereco, tel_motorista, email, senha)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (nome, cpf, cnh, cnpj, cidade, endereco, telefone, email, senha)

            # Executar a instrução SQL e fazer commit
            mycursor.execute(sql, valores)

            self.nome = nome
            self.cpf = cpf
            self.endereco = endereco
            self.tel = telefone
            self.email = email
            self.senha = senha

            mydb.commit()
            mycursor.close()
            mydb.close()
            return True
        except Exception as e:
            print(f"Erro: {e}")  # Para depuração
            return False
        
    def cadastrar_aluno(self, nome_aluno, condicao_medica, idade):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()
            
            sql = """
            INSERT INTO tb_alunos (nome_aluno, foto_aluno, condicao_medica, idade, responsavel_aluno)
            VALUES (%s, %s, %s, %s, %s)
            """
            valores = (nome_aluno, condicao_medica, idade)

            # Executar a instrução SQL e fazer commit
            mycursor.execute(sql, valores)

            mydb.commit()
            mycursor.close()
            mydb.close()
            return True
        except Exception as e:
            print(f"Erro: {e}")  # Para depuração
            return False

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
