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

            # Buscando o nome do aluno na tabela tb_alunos
            sql_busca_nome = """
            SELECT nome_aluno 
            FROM tb_alunos 
            WHERE id_aluno = %s;
            """
            mycursor.execute(sql_busca_nome, (id_aluno,))
            resultado = mycursor.fetchone()

            if resultado is None:
                print("Aluno não encontrado.")
                return False

            nome_aluno = resultado[0]  # Captura o nome do aluno

            # Inserindo na tabela historico_pagamentos
            sql = """
            INSERT INTO historico_pagamentos (id_aluno, nome_aluno, data_pagamento, mes_pagamento, valor_pagamento, cpf_motorista)
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            mycursor.execute(sql, (id_aluno, nome_aluno, data, mes, float(valor), cpf_motorista))

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

            # SQL sem o filtro de mês
            sql = "SELECT nome_aluno, mes_pagamento, data_pagamento, valor_pagamento FROM historico_pagamentos"

            mycursor.execute(sql)
            resultados = mycursor.fetchall()
            historico = []

            # Iterando sobre os resultados e adicionando ao histórico
            for linha in resultados:
                historico.append({
                    "nome_aluno": linha[0],
                    "mes_pagamento": linha[1],
                    "data_pagamento": linha[2],
                    "valor_pagamento": linha[3]
                })

            mydb.close()
            return historico
        except Exception as e:
            print(f"Erro ao listar histórico: {e}")
            return False
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