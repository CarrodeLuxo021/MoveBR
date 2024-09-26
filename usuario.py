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
        self.ft_motorista = None
        self.ft_veiculo = None
        self.valor_cobrado = None


    def cadastrar_motorista(self, nome, cpf, cnh, cnpj, telefone,  email, senha, cidade, foto_motorista, foto_van, valor_cobrado):
        try:

            mydb = Conexao.conectar()
            mycursor = mydb.cursor(prepared=True)

            sql = """
            INSERT INTO tb_motoristas (nome_motorista, cpf_motorista, cnh, cnpj, tel_motorista, email_motorista, senha_motorista, cidade_motorista, foto_van, foto_motorista, valor_cobrado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (nome, cpf, cnh, cnpj, telefone, email, senha, cidade, foto_motorista, foto_van, valor_cobrado)
            mycursor.execute(sql, values)

# ... (restante do código permanece o mesmo)
    

            self.nome = nome
            self.cpf = cpf
            self.cnh = cnh
            self.ft_motorista = foto_motorista
            self.ft_veiculo = foto_van
            self.valor_cobrado = valor_cobrado                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
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


    
