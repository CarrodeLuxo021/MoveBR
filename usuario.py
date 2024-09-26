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
        self.logado = False

    def cadastrar(self, nome, cpf, cnh, cnpj, telefone,  email, senha, cidade):
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

            sql = f"SELECT nome, cidade, tel_motorista FROM tb_motoristas"

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

    
