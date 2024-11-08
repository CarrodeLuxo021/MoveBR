from conexao import Conexao
import random
import string
from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify

class Usuario():
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.email = None
        self.logado = False

    def cadastrar_motorista(self, nome, cpf, telefone, email, senha):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"""INSERT INTO tb_motoristas (nome_motorista, cpf_motorista, tel_motorista, email_motorista, senha_motorista)
                    VALUES (%s, %s, %s, %s, %s);"""
            mycursor.execute(sql, (nome, cpf, telefone, email, senha))
            mydb.commit()
            mycursor.close()
            return True

        except Exception as e:
            print(f"Erro ao cadastrar motorista: {e}")
            return False

    def cadastrar_aluno(self, nome_aluno, foto_aluno, condicao_medica, escola, nome_responsavel, nome_reponsavel_2, endereco_responsavel, tel_responsavel, tel_responsavel_2, email_responsavel, serie_aluno, periodo_aluno):
        # try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # Inserir o aluno na tabela tb_alunos
            sql_aluno = """
            INSERT INTO tb_alunos (nome_aluno, foto_aluno, condicao_medica, escola, nome_responsavel, nome_reponsavel_2, endereco, telefone_responsavel, telefone_responsavel_2, email_responsavel, serie_aluno, periodo) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values_aluno = (nome_aluno, foto_aluno, condicao_medica, escola, nome_responsavel, nome_reponsavel_2, endereco_responsavel, tel_responsavel,tel_responsavel_2, email_responsavel, serie_aluno, periodo_aluno)
            mycursor.execute(sql_aluno, values_aluno)
            
            # Obtenha o ID do aluno recém-inserido
            id_aluno = mycursor.lastrowid
            
            # Obtenha o cpf_motorista da sessão
            cpf_motorista = session['usuario_logado']['cpf']
            
            # Inserir o contrato na tabela contratos_fechados
            sql_contrato = """
            INSERT INTO contratos_fechados (id_aluno, cpf_motorista) 
            VALUES (%s, %s)
            """
            values_contrato = (id_aluno, cpf_motorista)
            mycursor.execute(sql_contrato, values_contrato)

            mydb.commit()
            mycursor.close()
            mydb.close()

            return True
        
        # except Exception as e:
        #     print(f"Erro ao cadastrar aluno e fechar contrato: {e}")
        #     return False

    def logar(self, email, senha):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = "SELECT nome_motorista, cpf_motorista, email_motorista FROM tb_motoristas WHERE email_motorista = %s AND senha_motorista = %s"
            values = (email, senha)
            mycursor.execute(sql, values)
            resultado = mycursor.fetchone()
            
            if resultado:
                self.nome = resultado[0]
                self.cpf = resultado[1]
                self.email = resultado[2]
                self.logado = True
            else:
                self.logado = False

            mycursor.close()
            mydb.close()
            return self.logado
        except Exception as e:
            print(f"Erro ao logar: {e}")
            return False

    def listar_aluno(self):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = "SELECT nome_aluno, foto_aluno, condicao_medica, escola, telefone_responsavel, nome_responsavel, endereco, id_aluno FROM tb_alunos"
            mycursor.execute(sql)
            resultados = mycursor.fetchall()

            alunos = []
            for linha in resultados:
                alunos.append({
                    "nome_aluno": linha[0],
                    "foto_aluno": linha[1],
                    "condicao_medica": linha[2],
                    "escola": linha[3],
                    "telefone_responsavel": linha[4],
                    "nome_responsavel": linha[5],
                    "endereco": linha[6],
                    "id_aluno": linha[7]
                })
    
            mydb.close()
            return alunos
        except Exception as e:
            print(f"Erro ao listar alunos: {e}")
            return False

    def listar_aluno_por_escola(self, nome_escola):
        """Lista alunos por escola específica."""
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = "SELECT nome_aluno, foto_aluno, condicao_medica, escola, telefone_responsavel, nome_responsavel, endereco, id_aluno FROM tb_alunos WHERE escola = %s"
            mycursor.execute(sql, (nome_escola,))
            resultados = mycursor.fetchall()

            alunos = []
            for linha in resultados:
                alunos.append({
                    "nome_aluno": linha[0],
                    "foto_aluno": linha[1],
                    "condicao_medica": linha[2],
                    "escola": linha[3],
                    "telefone_responsavel": linha[4],
                    "nome_responsavel": linha[5],
                    "endereco": linha[6],
                    "id_aluno": linha[7]
                })

            mydb.close()
            return alunos
        except Exception as e:
            print(f"Erro ao listar alunos por escola: {e}")
            return False

    def listar_contratos_motorista(self):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # Obtenha o cpf_motorista da sessão
            cpf_motorista = session['usuario_logado']['cpf']

            # Busca os ids dos alunos nos contratos fechados para o motorista logado
            sql_contratos = """
            SELECT id_aluno FROM contratos_fechados WHERE cpf_motorista = %s
            """
            mycursor.execute(sql_contratos, (cpf_motorista,))
            ids_alunos = mycursor.fetchall()

            if not ids_alunos:
                return []  # Se não houver alunos, retorna uma lista vazia

            # Converte a lista de tuplas de ids em uma lista simples
            ids_alunos = [id_aluno[0] for id_aluno in ids_alunos]

            # Busca os dados dos alunos na tabela tb_alunos usando os ids encontrados
            placeholders = ','.join(['%s'] * len(ids_alunos))
            sql_alunos = f"""
            SELECT id_aluno, nome_aluno, foto_aluno, condicao_medica, escola, nome_responsavel, endereco, telefone_responsavel, email_responsavel 
            FROM tb_alunos WHERE id_aluno IN ({placeholders})
            """
            mycursor.execute(sql_alunos, tuple(ids_alunos))
            resultados = mycursor.fetchall()

            # Formata os resultados em um dicionário
            alunos = []
            for linha in resultados:
                alunos.append({
                    "id_aluno": linha[0],
                    "nome_aluno": linha[1],
                    "foto_aluno": linha[2],
                    "condicao_medica": linha[3],
                    "escola": linha[4],
                    "nome_responsavel": linha[5],
                    "endereco": linha[6],
                    "telefone_responsavel": linha[7],
                    "email_responsavel": linha[8]
                })

            mydb.close()
            return alunos  # Retorna os dados dos alunos

        except Exception as e:
            print(f"Erro ao listar contratos fechados: {e}")
            return []
    
    def excluir_aluno(self, id_aluno):
        try:
            # Conectar ao banco de dados
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            # Excluir da tabela contratos_fechados
            sql_contratos = "DELETE FROM contratos_fechados WHERE id_aluno = %s"
            mycursor.execute(sql_contratos, (id_aluno,))

            # Excluir da tabela tb_alunos
            sql_alunos = "DELETE FROM tb_alunos WHERE id_aluno = %s"
            mycursor.execute(sql_alunos, (id_aluno,))

            # Confirmar as alterações no banco de dados
            mydb.commit()

            # Fechar conexão com o banco
            mydb.close()

            return True  # Retorna True para indicar sucesso

        except Exception as e:
            print(f"Erro ao excluir o aluno: {e}")
            return False  # Retorna False em caso de erro

    def listar_aluno_por_nome(self, nome):
        # Conectar ao banco de dados e buscar alunos com base no nome
        conn = Conexao.conectar()
        cursor = conn.cursor(dictionary=True)
        
        query = "SELECT * FROM tb_alunos WHERE nome_aluno LIKE %s"
        cursor.execute(query, ('%' + nome + '%',))  # Pesquisa com LIKE para encontrar qualquer aluno com o nome informado

        alunos = cursor.fetchall()  # Recupera os resultados da pesquisa
        conn.close()
        return alunos
    
    def pesquisar_aluno(self, pesquisa):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"SELECT nome_aluno, foto_aluno, condicao_medica, escola, telefone_responsavel, nome_responsavel, endereco FROM tb_alunos WHERE escola = '{pesquisa}'"
            mycursor.execute(sql)
            resultados = mycursor.fetchall()

            alunosf = []
            for aluno in resultados:
                alunosf.append({
                    "nome_aluno": aluno[0],
                    "foto_aluno": aluno[1],
                    "condicao_medica": aluno[2],
                    "escola": aluno[3],
                    "telefone_responsavel": aluno[4],
                    "nome_responsavel": aluno[5],
                    "endereco": aluno[6]
                })
    

            
            mydb.close()
            return alunosf
        except Exception as e:
            print(f"Erro ao pesquisar aluno: {e}")
            return False
        
    def gerar_codigo(tamanho=8):
        
        mydb = Conexao.conectar()
        mycursor = mydb.cursor()
        
        """Gera um código aleatório de tamanho especificado."""
        caracteres = string.ascii_letters + string.digits  # Letras e dígitos
        codigo = ''.join(random.choice(caracteres) for _ in range(tamanho))
        
        mycursor.execute("INSERT INTO tb_codigos (codigo) VALUES (%s)", (codigo,))
        mydb.commit()
        mydb.close()
        
        """ link = f"http://bdmovebr.mysql.database.azure.com/cadastrar-aluno/{codigo}" """
        link = f"http://127.0.0.1:8080/cadastrar-aluno/{codigo}"
        
        return link
    
    def verficar_codigo(self, codigo):
        mydb = Conexao.conectar()
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT codigo FROM tb_codigos")
        codigos = mycursor.fetchall()
        
        
        lista_codigos = [codigo[0] for codigo in codigos]

        for codigo in lista_codigos:
            if codigo in lista_codigos:
                mycursor.execute("UPDATE tb_codigos SET verificacao = 'indisponivel' WHERE codigo = %s", (codigo,))
                return True
            else:
                mycursor.execute("UPDATE tb_codigos SET verificacao = 'disponivel' WHERE codigo = %s", (codigo,))
                return False
        
        mydb.close()
        mycursor.close()
            
       
