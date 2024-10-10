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

        # Buscando o nome do aluno na tabela tb_alunos
        sql_busca_nome = """
        SELECT nome_aluno 
        FROM tb_alunos 
        WHERE id_aluno = %s;
        """
        mycursor.execute(sql_busca_nome, (id_aluno,))
        nome_aluno = mycursor.fetchone()[0]  # Captura o nome do aluno

        # Inserindo na tabela historico_pagamentos
        sql = """
        INSERT INTO historico_pagamentos (id_aluno, nome_aluno, data_pagamento, mes_pagamento, valor_pagamento)
        VALUES (%s, %s, %s, %s, %s);
        """
        mycursor.execute(sql, (id_aluno, nome_aluno, data, mes, valor))

        mydb.commit()
        mycursor.close()

        return True

    except Exception as e:
        print(f"Erro ao cadastrar pagamento: {e}")
        return False