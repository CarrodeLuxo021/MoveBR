from conexao import Conexao
class Pagamentos():
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.email = None
        self.logado = False

    def gerar_pagamento(self, id_aluno, mes, data, valor):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # Primeiro, você faz um JOIN para buscar o nome do aluno na tabela tb_alunos
            sql_busca_nome = f"""
            SELECT nome_aluno 
            FROM tb_alunos 
            WHERE id_aluno = {id_aluno};
            """
            mycursor.execute(sql_busca_nome)
            nome_aluno = mycursor.fetchone()[0]  # Captura o nome do aluno

            # Agora, você insere na tabela historico_pagamentos com o nome do aluno
            sql = f"""
            INSERT INTO historico_pagamentos (id_aluno, nome_aluno, data_pagamento, mes_pagamento, valor_pagamento)
            VALUES ('{id_aluno}', '{nome_aluno}', '{data}', '{mes}', '{valor}');
            """
            mycursor.execute(sql)

            mydb.commit()
            mycursor.close()

            return True

        except Exception as e:
            print(f"Erro ao cadastrar pagamento: {e}")
            return False
        
    def listar_historico(self, mes, cpf_motorista):
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