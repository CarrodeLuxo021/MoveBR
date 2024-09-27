from conexao import Conexao

class Usuario():
    def __init__(self):
        self.nome = None
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


    def cadastrar(self, nome, cpf, cnh, cnpj, cidade, endereco, telefone, email, senha):
        try:

            mydb = Conexao.conectar()
            mycursor = mydb.cursor(prepared=True)

            sql = f"""
            INSERT INTO tb_motoristas (nome, cpf, cnh, cnpj, cidade, endereco, m_periodos, tel_motorista, email, senha)
            VALUES ('{nome}', '{cpf}', '{cnh}', '{cnpj}', '{cidade}', '{endereco}', '{telefone}', '{email}', '{senha}')
            """
            mycursor.execute(sql)  

            self.nome = nome
            self.cpf = cpf
            self.cnh = cnh
            self.cnpj = cnpj
            self.cidade = cidade
            self.endereco = endereco
            self.tel = telefone
            self.email = email
            self.senha = senha

            
            mydb.commit()
            mycursor.close()

            return True
        
        except Exception as e:

            print(f"Erro ao cadastrar motorista: {e}")
            return False
        
    def cadastrar_aluno(self, nome_aluno, endereco, cidade, idade, nome_responsavel, tel_responsavel):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"""
            INSERT INTO tb_alunos (nome_aluno, endereco, cidade, idade, nome_responsavel, tel_responsavel)
            VALUES ('{nome_aluno}', '{endereco}', '{cidade}', '{idade}', '{nome_responsavel}', '{tel_responsavel}')
            """
            mycursor.execute(sql)

            self.nome_aluno = nome_aluno
            self.endereco = endereco
            self.cidade = cidade
            self.idade = idade
            self.nome_responsavel = nome_responsavel
            self.tel_responsavel = tel_responsavel


            mydb.commit()
            mycursor.close()
            return True
        except:
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


    
