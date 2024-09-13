from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify, self
from conexao import Conexao
from usuario import Usuario

class Usuario():
    def __init__(self):
        self.nome_responsavel = None
        self.email_responsavel = None
        self.senha_responsavel = None
        self.tel_responsavel = None
        self.endereco_responsavel = None
        self.cpf_responsavel = None

        self.logado_responsavel = False

def cadastrar(nome_responsavel, endereco_responsavel, tel_responsavel, cpf_responsavel, email_responsavel, senha_responsavel):
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

        self.nome = nome
        self.cpf = cpf
        self.cnh = cnh
        self.cnpj = cnpj
        self.cidade = cidade
        self.endereco = endereco
        self.tel = telefone
        self.email = email
        self.senha = senha

        
        mydb.commit()
        mydb.close()
        return True
    except:
        return False
        
def cadastrar_aluno(self, nome_aluno, endereco, cidade, idade, nome_responsavel, tel_responsavel):
    try:
        mydb = Conexao.conectar()
        mycursor = mydb.cursor()

        sql = f"""
        INSERT INTO tb_alunos (nome_aluno, endereco, cidade, idade, nome_responsavel, tel_responsavel)
        VALUES ('{nome_aluno}', '{endereco}', '{cidade}', '{idade}', '{nome_responsavel}', '{tel_responsavel}')
        """
        mycursor.execute(sql)

        self.nome_aluno = nome_aluno
        self.endereco = endereco
        self.cidade = cidade
        self.idade = idade
        self.nome_responsavel = nome_responsavel
        self.tel_responsavel = tel_responsavel


        mydb.commit()
        mydb.close()
        return True
    except:
        return False

def listar_usuario():
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
