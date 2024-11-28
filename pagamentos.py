from conexao import Conexao
class Pagamentos():
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.email = None
        self.logado = False

    def gerar_pagamento(self, id_aluno, mes, data, valor, metodo_pagamento, cpf_motorista):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # Inserindo na tabela historico_pagamentos
            sql = """
            INSERT INTO historico_pagamentos 
            (id_aluno, data_pagamento, mes_pagamento, valor_pagamento, metodo_pagamento, cpf_motorista)
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            mycursor.execute(sql, (id_aluno, data, mes, valor, metodo_pagamento, cpf_motorista))

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

            # SQL para buscar os pagamentos junto com o nome dos alunos e método de pagamento
            sql = """
            SELECT tb_alunos.nome_aluno, historico_pagamentos.metodo_pagamento, historico_pagamentos.data_pagamento, 
                historico_pagamentos.valor_pagamento, historico_pagamentos.id_aluno, historico_pagamentos.id_pagamento
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
                    "metodo_pagamento": linha[1],  # Substituindo o mês pelo método
                    "data_pagamento": linha[2],
                    "valor_pagamento": linha[3],
                    "id_aluno": linha[4],
                    "id_pagamento": linha[5],
                })

            mydb.close()
            return historico

        except Exception as e:
            print(f"Erro ao listar histórico: {e}")
            return False
        
    def listar_historico_filtro(self, metodo, cpf_motorista):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            if metodo:
                sql = """
                SELECT id_pagamento, nome_aluno, metodo_pagamento, data_pagamento, valor_pagamento, id_aluno 
                FROM historico_pagamentos 
                WHERE metodo_pagamento = %s AND cpf_motorista = %s
                """
                mycursor.execute(sql, (metodo, cpf_motorista))
            else:
                # Se o método for None, seleciona todos os pagamentos do motorista
                sql = """
                SELECT id_pagamento, nome_aluno, metodo_pagamento, data_pagamento, valor_pagamento, id_aluno 
                FROM historico_pagamentos 
                WHERE cpf_motorista = %s
                """
                mycursor.execute(sql, (cpf_motorista,))

            resultados = mycursor.fetchall()
            historico = [{
                "id_pagamento": linha[0],
                "nome_aluno": linha[1],
                "metodo_pagamento": linha[2],  # Alteração para exibir o método
                "data_pagamento": linha[3],
                "valor_pagamento": linha[4],
                "id_aluno": linha[5]
            } for linha in resultados]

            mydb.close()
            return historico

        except Exception as e:
            print(f"Erro ao listar histórico: {e}")
            return []

    def listar_alunos_pendentes(self, mes, cpf_motorista):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()
            
            # Verifica se o mês foi especificado
            if mes:
                sql = """
                SELECT a.nome_aluno, a.id_aluno
                FROM tb_alunos AS a
                INNER JOIN contratos_fechados AS c ON a.id_aluno = c.id_aluno
                LEFT JOIN historico_pagamentos AS hp 
                ON a.id_aluno = hp.id_aluno AND hp.mes_pagamento = %s
                WHERE c.cpf_motorista = %s AND hp.id_pagamento IS NULL;
                """
                mycursor.execute(sql, (mes, cpf_motorista))
            else:
                # Caso o mês não seja especificado, retorna lista vazia
                return []
            
            resultados = mycursor.fetchall()
            alunos_pendentes = [{"nome_aluno": linha[0], "id_aluno": linha[1]} for linha in resultados]

            mydb.close()
            return alunos_pendentes
        except Exception as e:
            print(f"Erro ao listar alunos pendentes: {e}")
            return []
        
    def excluir_historico(self, id_pagamento):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # Deletando o pagamento pelo ID correto
            sql = "DELETE FROM historico_pagamentos WHERE id_pagamento = %s"
            mycursor.execute(sql, (id_pagamento,))
            mydb.commit()
            mycursor.close()
            return True

        except Exception as e:
            print(f"Erro ao excluir pagamento: {e}")
            return False
        