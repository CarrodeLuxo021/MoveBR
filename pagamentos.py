from conexao import Conexao
class Pagamentos():
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.email = None
        self.logado = False

    def gerar_pagamento(self, id_aluno, nome_aluno, mes, data, valor, metodo_pagamento, cpf_motorista):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # Se o nome_aluno não foi passado, consulte na tabela tb_alunos
            if not nome_aluno:
                # Consultar o nome do aluno com base no id_aluno
                sql_nome = "SELECT nome_aluno FROM tb_alunos WHERE id_aluno = %s"
                mycursor.execute(sql_nome, (id_aluno,))
                result = mycursor.fetchone()

                if result:
                    nome_aluno = result[0]  # Pega o nome_aluno retornado da consulta
                else:
                    print(f"Aluno com id {id_aluno} não encontrado.")
                    return False

            # Inserir os dados na tabela historico_pagamentos
            sql = """
            INSERT INTO historico_pagamentos 
            (id_aluno, nome_aluno, data_pagamento, mes_pagamento, valor_pagamento, metodo_pagamento, cpf_motorista)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            mycursor.execute(sql, (id_aluno, nome_aluno, data, mes, valor, metodo_pagamento, cpf_motorista))

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
                    "nome_aluno": linha[0],               # Nome do aluno (da tabela tb_alunos)
                    "metodo_pagamento": linha[1],         # Método de pagamento
                    "data_pagamento": linha[2],           # Data do pagamento
                    "valor_pagamento": linha[3],          # Valor do pagamento
                    "id_aluno": linha[4],                 # ID do aluno
                    "id_pagamento": linha[5],             # ID do pagamento
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

            # Se 'mes' for fornecido, filtra pelo mês e CPF do motorista
            if mes:
                sql = """
                SELECT historico_pagamentos.id_pagamento, tb_alunos.nome_aluno, historico_pagamentos.metodo_pagamento, 
                    historico_pagamentos.data_pagamento, historico_pagamentos.valor_pagamento, historico_pagamentos.id_aluno
                FROM historico_pagamentos
                INNER JOIN tb_alunos ON historico_pagamentos.id_aluno = tb_alunos.id_aluno
                WHERE historico_pagamentos.mes_pagamento = %s AND historico_pagamentos.cpf_motorista = %s
                """
                mycursor.execute(sql, (mes, cpf_motorista))
            else:
                # Se 'mes' for None, seleciona todos os pagamentos do motorista
                sql = """
                SELECT historico_pagamentos.id_pagamento, tb_alunos.nome_aluno, historico_pagamentos.metodo_pagamento, 
                    historico_pagamentos.data_pagamento, historico_pagamentos.valor_pagamento, historico_pagamentos.id_aluno
                FROM historico_pagamentos
                INNER JOIN tb_alunos ON historico_pagamentos.id_aluno = tb_alunos.id_aluno
                WHERE historico_pagamentos.cpf_motorista = %s
                """
                mycursor.execute(sql, (cpf_motorista,))

            resultados = mycursor.fetchall()
            historico = [{
                "id_pagamento": linha[0],
                "nome_aluno": linha[1],  # Nome do aluno vindo da tabela tb_alunos
                "metodo_pagamento": linha[2],
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
        