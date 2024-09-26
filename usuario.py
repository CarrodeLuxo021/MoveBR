from conexao import Conexao

class Usuario():
    def __init__(self):
        self.tel = None
        self.nome = None
        self.senha = None
        self.endereco = None
        self.cpf = None
        self.cidade = None
        self.email = None
        self.escola = None
        self.idade = None
        self.logado = False
        self.foto_aluno = None
        self.condicao_medica = None


    def cadastrar_motorista(self, nome, cpf, cnh, cnpj, telefone,  email, senha, cidade):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"""
            INSERT INTO tb_motoristas (nome, cpf, cnh, cnpj, tel_motorista, email, senha, cidade)
            VALUES ('{nome}', '{cpf}', '{cnh}', '{cnpj}',  '{telefone}', '{email}', '{senha}', '{cidade}')
            """
            mycursor.execute(sql)  

            self.nome = nome
            self.cpf = cpf
            self.cnh = cnh
            self.cnpj = cnpj
            self.tel = telefone
            self.email = email
            self.senha = senha
            self.cidade = cidade

            
            mydb.commit()
            mydb.close()
            return True
        except:
            return False
        
    def cadastrar_aluno(self, nome, escola,foto_aluno, condicao_medica, nome_responsavel,  tel_responsavel):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"""
            INSERT INTO tb_alunos (nome_aluno, escola,foto_aluno, condicao_medica, nome_responsavel, tel_responsavel)
            VALUES ('{nome}', '{foto_aluno}', '{condicao_medica}', '{escola}',  '{nome_responsavel}', '{tel_responsavel}')
            """
            mycursor.execute(sql)  

            self.nome = nome
            self.condicao_medica = condicao_medica
            self.foto_aluno = foto_aluno
            self.escola = escola
            self.nome = nome_responsavel
            self.tel = tel_responsavel

            
            mydb.commit()
            mydb.close()
            return True
        except:
            return False
        
    def logar(self, senha, email):
        mydb = Conexao.conectar()
        mycursor = mydb.cursor()
        
        
        sql = f"SELECT tel_motorista, nome, senha, cpf FROM tb_motoristas WHERE email='{email}' AND senha='{senha}'"
        
        mycursor.execute(sql)
    
        resultado = mycursor.fetchone()
        print(resultado)
        if not resultado == None:
            self.logado = True
            self.cpf = resultado[3]
            self.nome = resultado[1]
            self.tel = resultado[0]
            self.senha = resultado[2]
        else:
            self.logado = False
        

    def listar_usuario(self):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"SELECT nome, cidade, tel_motorista FROM tb_alunos"

            mycursor.execute(sql)
            resultados = mycursor.fetchall()
            alunos = []
            for linha in resultados:
                alunos.append({
                    "nome": linha[0],
                    "cidade": linha[1],
                    "tel_motorista": linha[2]
                })
            mycursor.close()
            mydb.close()
            return alunos
        except:
            return False
    
    def listar_aluno(self):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"SELECT nome_aluno, cidade, nome_responsavel FROM tb_alunos;"

            mycursor.execute(sql)
            resultados = mycursor.fetchall()
            alunos = []
            for linha in resultados:
                alunos.append({
                    "nome": linha[0],
                    "cidade": linha[1],
                    "nome_responsavel": linha[2]
                })
            mycursor.close()
            mydb.close()
            return alunos
        except:
            return False


    
