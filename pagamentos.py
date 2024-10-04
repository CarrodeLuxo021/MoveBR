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