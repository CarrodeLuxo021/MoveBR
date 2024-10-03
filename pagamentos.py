from conexao import Conexao

class Pagamentos():
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.email = None
        self.logado = False

    def gerar_pagamento(self, nome_aluno, mes, data, valor):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"""INSERT INTO historico_pagamentos (nome_motorista, cpf_motorista, cnh, cnpj, tel_motorista, email_motorista, senha_motorista)
            VALUES ('{nome}', '{cpf}', '{cnh}', '{cnpj}', '{telefone}', '{email}', '{senha}');
            """
            mycursor.execute(sql)

            mydb.commit()
            mycursor.close()