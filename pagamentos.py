from conexao import Conexao
class Pagamentos():
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.email = None
        self.logado = False

    def gerar_pagamento(self, id_aluno, data, mes, valor, id_motorista):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # Adiciona o id_motorista à query de inserção
            sql = f"""INSERT INTO historico_pagamentos (id_aluno, data_pagamento, mes_pagamento, valor_pagamento, id_motorista)
                      VALUES ('{id_aluno}', '{data}', '{mes}', '{valor}', '{id_motorista}');
                   """
            mycursor.execute(sql)

            mydb.commit()
            mycursor.close()

            return True
        
        except Exception as e:
            print(f"Erro ao cadastrar pagamento: {e}")
            return False