from conexao import Conexao
from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify

class Usuario():
    def __init__(self):
        self.nome = None
        self.email = None
        self.senha = None
        self.telefone = None
        self.endereco = None
        self.cpf = None
        self.logado = False

    def cadastrar_responsaveis(self, nome_responsavel, endereco_responsavel, tel_responsavel, cpf_responsavel, email_responsavel, senha_responsavel):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()
                # Instrução SQL corrigida para a tabela tb_responsavel
            sql = """
            INSERT INTO tb_responsavel (nome_responsavel, endereco_responsavel, tel_responsavel, cpf_responsavel, email_responsavel, senha_responsavel)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (nome_responsavel, endereco_responsavel, tel_responsavel, cpf_responsavel, email_responsavel, senha_responsavel)

            # Executar a instrução SQL e fazer commit
            mycursor.execute(sql, valores)  

            self.nome = nome_responsavel
            self.cpf = cpf_responsavel
            self.endereco = endereco_responsavel
            self.tel = tel_responsavel
            self.email = email_responsavel
            self.senha = senha_responsavel

            
            mydb.commit()
            mydb.close()
            return True
        except:
            return False
    
    def cadastrar_motorista(self, nome, endereco, cidade, cpf, cnh, cnpj, telefone, email, senha):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()
            
            sql = """
            INSERT INTO tb_motoristas ( , email, senha)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (nome, cpf, cnh, cnpj, cidade, endereco, telefone, email, senha)

            # Executar a instrução SQL e fazer commit
            mycursor.execute(sql, valores)

            self.nome = nome
            self.cpf = cpf
            self.endereco = endereco
            self.tel = telefone
            self.email = email
            self.senha = senha

            mydb.commit()
            mycursor.close()
            mydb.close()
            return True
        except Exception as e:
            print(f"Erro: {e}")  # Para depuração
            return False
        
    def cadastrar_aluno(self, nome_aluno, condicao_medica, idade):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()
            
            sql = """
            INSERT INTO tb_alunos (nome_aluno, foto_aluno, condicao_medica, idade, responsavel_aluno)
            VALUES (%s, %s, %s, %s, %s)
            """
            valores = (nome_aluno, condicao_medica, idade)

            # Executar a instrução SQL e fazer commit
            mycursor.execute(sql, valores)

            mydb.commit()
            mycursor.close()
            mydb.close()
            return True
        except Exception as e:
            print(f"Erro: {e}")  # Para depuração
            return False


    def logar_resposavel(self, email, senha):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()
            sql = "SELECT cpf_responsavel FROM tb_responsavel WHERE email_responsavel = %s AND senha_responsavel = %s"
            # Executa a consulta SQL com os parâmetros fornecidos
            mycursor.execute(sql, (email, senha))
            resultado = mycursor.fetchone()
            if resultado:
                session['cpf_responsavel'] = {
                    "nome_responsavel": resultado['nome_responsavel'],
                    "telefone_responsavel": resultado['tel_responsavel'],
                    "cpf_responsavel": resultado['cpf_responsavel']
                }
                return True
            else:
                # Se as credenciais forem inválidas, exibe uma mensagem de erro e reexibe o formulário de login
                flash("Credenciais inválidas")
                return False
        except:
            return False
    
    def logar_motorista(self, email, senha):
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()
            sql = "SELECT cpf_motorista FROM tb_motorista WHERE email_motorista = %s AND senha_motorista = %s"
            # Executa a consulta SQL com os parâmetros fornecidos
            mycursor.execute(sql, (email, senha))
            resultado = mycursor.fetchone()
            if resultado:
                session['cpf_motorista'] = {
                    "nome_motorista": resultado['nome_motorista'],
                    "telefone_motorista": resultado['tel_motorista'],
                    "cpf_motorista": resultado['cpf_motorista']
                }
                return True
            else:
                # Se as credenciais forem inválidas, exibe uma mensagem de erro e reexibe o formulário de login
                flash("Credenciais inválidas")
                return False
        except:
            return False
        
    def listar_alunos():
        try:
            mydb = Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"SELECT  FROM tb_alunos"

            mycursor.execute(sql)
            mycursor.fetchall()
            resultados = mycursor.fetchall()
            alunos = []
            for linha in resultados:
                alunos.append({"id_aluno":linha[0],
                                })
                for dados in linha:
                    print(dados)
                    mycursor.close()
                    mydb.close()
            return True
        except:
            return False
