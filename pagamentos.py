from conexao import Conexao
class Pagamentos():
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.email = None
        self.logado = False

    def gerar_pagamento(self, id_aluno, mes, data, valor, cpf_motorista):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # Inserindo na tabela historico_pagamentos
            sql = """
            INSERT INTO historico_pagamentos (id_aluno, data_pagamento, mes_pagamento, valor_pagamento, cpf_motorista)
            VALUES (%s, %s, %s, %s, %s);
            """
            mycursor.execute(sql, (id_aluno, data, mes, float(valor), cpf_motorista))

            mydb.commit()
            mycursor.close()
            return True

        except Exception as e:
            mydb.rollback()
            print(f"Erro ao cadastrar pagamento: {e}")


    def listar_historico(self):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # Consulta SQL para listar os pagamentos e informações dos alunos
            sql = """
            SELECT tb_alunos.nome_aluno, historico_pagamentos.mes_pagamento, historico_pagamentos.data_pagamento, 
                historico_pagamentos.valor_pagamento, historico_pagamentos.id_pagamento
            FROM historico_pagamentos
            INNER JOIN tb_alunos ON historico_pagamentos.id_aluno = tb_alunos.id_aluno;
            """

            mycursor.execute(sql)
            resultados = mycursor.fetchall()

            # Formatação dos resultados em uma lista de dicionários
            historico = []
            for linha in resultados:
                historico.append({
                    "nome_aluno": linha[0],
                    "mes_pagamento": linha[1],
                    "data_pagamento": linha[2],
                    "valor_pagamento": linha[3],
                    "id_pagamento": linha[4]
                })

            return historico

        except Exception as e:
            print(f"Erro ao listar histórico: {e}")
            return []

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()
           
    def listar_historico_filtro(self, mes, cpf_motorista):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"SELECT * from historico_pagamentos where mes_pagamento = {mes} and cpf_motorista = {cpf_motorista} "

            mycursor.execute(sql)
            resultados = mycursor.fetchall()
            historico = []
            for linha in resultados:
                historico.append({"nome_aluno":linha[0],
                               "mes_pagamento": linha[1],
                               "data_pagamento": linha[2],
                               "valor_pagamento": linha[3]
                })
    
            mydb.close()
            return historico
        except:
            return False
        
    