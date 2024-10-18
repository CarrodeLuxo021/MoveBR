from conexao import Conexao
from flask import  session

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
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # Inserir o aluno na tabela tb_alunos
            sql_aluno = """
            INSERT INTO tb_alunos (nome_aluno, foto_aluno, condicao_medica, escola, nome_responsavel, endereco, telefone_responsavel, email_responsavel) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values_aluno = (nome_aluno, foto_aluno, condicao_medica, escola, nome_responsavel, endereco_responsavel, tel_responsavel, email_responsavel)
            mycursor.execute(sql_aluno, values_aluno)
            
            # Obtenha o ID do aluno recém-inserido
            id_aluno = mycursor.lastrowid
            
            # Obtenha o cpf_motorista da sessão
            cpf_motorista = session['usuario_logado']['cpf']
            
            # Inserir o contrato na tabela contratos_fechados
            sql_contrato = """
            INSERT INTO contratos_fechados (id_aluno, cpf_motorista) 
            VALUES (%s, %s)
            """
            values_contrato = (id_aluno, cpf_motorista)
            mycursor.execute(sql_contrato, values_contrato)

            mydb.commit()
            mycursor.close()
            mydb.close()

            return True
        
        except Exception as e:
            print(f"Erro ao cadastrar aluno e fechar contrato: {e}")
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
        
    def listar_contratos_motorista(self):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # Obtenha o cpf_motorista da sessão
            cpf_motorista = session['usuario_logado']['cpf']

            # Busca os ids dos alunos nos contratos fechados para o motorista logado
            sql_contratos = """
            SELECT id_aluno FROM contratos_fechados WHERE cpf_motorista = %s
            """
            mycursor.execute(sql_contratos, (cpf_motorista,))
            ids_alunos = mycursor.fetchall()

            if not ids_alunos:
                return []  # Se não houver alunos, retorna uma lista vazia

            # Converte a lista de tuplas de ids em uma lista simples
            ids_alunos = [id_aluno[0] for id_aluno in ids_alunos]

            # Busca os dados dos alunos na tabela tb_alunos usando os ids encontrados
            placeholders = ','.join(['%s'] * len(ids_alunos))
            sql_alunos = f"""
            SELECT id_aluno, nome_aluno, foto_aluno, condicao_medica, escola, nome_responsavel, endereco, telefone_responsavel, email_responsavel 
            FROM tb_alunos WHERE id_aluno IN ({placeholders})
            """
            mycursor.execute(sql_alunos, tuple(ids_alunos))
            resultados = mycursor.fetchall()

            # Formata os resultados em um dicionário
            alunos = []
            for linha in resultados:
                alunos.append({
                    "id_aluno": linha[0],
                    "nome_aluno": linha[1],
                    "foto_aluno": linha[2],
                    "condicao_medica": linha[3],
                    "escola": linha[4],
                    "nome_responsavel": linha[5],
                    "endereco": linha[6],
                    "telefone_responsavel": linha[7],
                    "email_responsavel": linha[8]
                })

            mydb.close()
            return alunos  # Retorna os dados dos alunos

        except Exception as e:
            print(f"Erro ao listar contratos fechados: {e}")
            return []
    
    def excluir_aluno(self, id_aluno):
        try:
            # Conectar ao banco de dados
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # Excluir da tabela contratos_fechados
            sql_contratos = "DELETE FROM contratos_fechados WHERE id_aluno = %s"
            mycursor.execute(sql_contratos, (id_aluno,))

            # Excluir da tabela historico_pagamentos
            sql_pagamentos = "DELETE FROM historico_pagamentos WHERE id_aluno = %s"
            mycursor.execute(sql_pagamentos, (id_aluno,))

            # Excluir da tabela tb_alunos
            sql_alunos = "DELETE FROM tb_alunos WHERE id_aluno = %s"
            mycursor.execute(sql_alunos, (id_aluno,))

            # Confirmar as alterações no banco de dados
            mydb.commit()

            # Fechar conexão com o banco
            mydb.close()

            return True  # Retorna True para indicar sucesso

        except Exception as e:
            print(f"Erro ao excluir o aluno: {e}")
            return False  # Retorna False em caso de erro
    
    def excluir_historico(self, id_aluno):

        mydb = Conexao.conectar()
        mycursor = mydb.cursor()

        sql = f"DELETE  FROM historico_pagamentos WHERE id_aluno = {id_aluno}"
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