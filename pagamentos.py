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

            sql = f"""INSERT INTO historico_pagamentos (id_aluno, data_pagamento, mes_pagamento, valor_pagamento)
            VALUES ('{id_aluno}', '{mes}', '{data}', '{valor}');
            """
            mycursor.execute(sql)

            mydb.commit()
            mycursor.close()

            return True
        
        except Exception as e:

            print(f"Erro ao cadastrar aluno: {e}")
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
                historico.append({"valor_pagamento":linha[0],
                               "mes_pagamento": linha[1],
                               "data_pagamento": linha[2],
                               "escola": linha[3],
                               "telefone_responsavel": linha[4],
                               "nome_responsavel": linha[5],
                               "endereco": linha[6]

                })
    
            mydb.close()
            return alunos
        except:
            return False