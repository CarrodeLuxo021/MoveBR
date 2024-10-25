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
            INSERT INTO historico_pagamentos 
            (id_aluno, data_pagamento, mes_pagamento, valor_pagamento, cpf_motorista)
            VALUES (%s, %s, %s, %s, %s);
            """
            mycursor.execute(sql, (id_aluno, data, mes, valor, cpf_motorista))

            mydb.commit()
            mycursor.close()
            return True

        except Exception as e:
            mydb.rollback()
            print(f"Erro ao cadastrar pagamento: {e}")
            return False


    def listar_historico(self):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # SQL para buscar os pagamentos junto com o nome dos alunos
            sql = """
            SELECT tb_alunos.nome_aluno, historico_pagamentos.mes_pagamento, historico_pagamentos.data_pagamento, 
                   historico_pagamentos.valor_pagamento, historico_pagamentos.id_aluno
            FROM historico_pagamentos
            INNER JOIN tb_alunos ON historico_pagamentos.id_aluno = tb_alunos.id_aluno;
            """

            mycursor.execute(sql)
            resultados = mycursor.fetchall()
            historico = []

            # Iterando sobre os resultados e adicionando ao histórico
            for linha in resultados:
                historico.append({
                    "nome_aluno": linha[0],
                    "mes_pagamento": linha[1],
                    "data_pagamento": linha[2],
                    "valor_pagamento": linha[3],
                    "id_aluno": linha[4]
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

            # Usando query parametrizada para evitar injeção de SQL
            sql = "SELECT nome_aluno, mes_pagamento, data_pagamento, valor_pagamento, id_aluno FROM historico_pagamentos WHERE mes_pagamento = %s AND cpf_motorista = %s"
            mycursor.execute(sql, (mes, cpf_motorista))

            resultados = mycursor.fetchall()
            historico = []
            for linha in resultados:
                historico.append({
                    "nome_aluno": linha[0],
                    "mes_pagamento": linha[1],
                    "data_pagamento": linha[2],
                    "valor_pagamento": linha[3],
                    "id_aluno": linha[4]  # Adicionei o campo id_aluno para o botão de excluir
                })

            mydb.close()
            return historico
        except Exception as e:
            print(f"Erro ao listar histórico: {e}")
            return False
        
    def excluir_historico(self, id_pagamento):
        mydb = Conexao.conectar()
        mycursor = mydb.cursor()

        sql = f"DELETE FROM historico_pagamentos WHERE id_pagamento = {id_pagamento}"
        mycursor.execute(sql)
        mydb.commit()
        mydb.close()
        return True
    