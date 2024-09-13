from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from conexao import Conexao
from usuario import Usuario


app = Flask(__name__)
app.secret_key = "banana"

@app.route("/")
def pag_inicio():
    return render_template('pag-inicial.html')


@app.route("/cadastrar-motorista", methods=["GET"])
def pag_cadastro_motorista():
    return render_template('pag-motorista.html')

@app.route("/cadastrar-aluno", methods=["GET"])
def pag_cadastro_aluno ():
    return render_template('cadastro-aluno.html')

@app.route("/cadastrar-motorista", methods=["POST"])
def cadastrar():

    nome = request.form["nome"]
    cpf = request.form["cpf"]
    cnpj = request.form["cnpj"]
    cnh = request.form["cnh"]
    telefone = request.form["telefone"]
    email = request.form["email"]
    senha = request.form["senha"]
    cidade = request.form["cidade"]
    endereco = request.form["endereco"]
    

    mydb = Conexao.conectar()

    mycursor = mydb.cursor()

    sql = f"""
    INSERT INTO tb_motoristas (nome, cpf, cnh, cnpj, cidade, endereco, tel_motorista, email, senha)
    VALUES ('{nome}', '{cpf}', '{cnh}', '{cnpj}', '{cidade}', '{endereco}', '{telefone}', '{email}', '{senha}')
    """

    mycursor.execute(sql)    
    mydb.commit()
    return render_template('pag-inicial.html')

from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

class Conexao:
    @staticmethod
    def conectar():
        return mysql.connector.connect(
            host="localhost",
            user="usuario",
            password="senha",
            database="nome_do_banco"
        )

@app.route("/cadastrar-responsavel", methods=["POST"])
def cadastrar_responsavel():
    nome_responsavel = request.form["nome_responsavel"]
    endereco_responsavel = request.form["endereco_responsavel"]
    tel_responsavel = request.form["tel_responsavel"]
    cpf_responsavel = request.form["cpf_responsavel"]
    email_responsavel = request.form["email_responsavel"]
    senha_responsavel = request.form["senha_responsavel"]

    # Conectar ao banco de dados
    

   
    mydb.commit()

    # Fechar o cursor e a conexão
    mycursor.close()
    mydb.close()

    # Renderizar a página de sucesso ou redirecionar conforme necessário
    return render_template('pag-inicial.html')


@app.route("/login-aluno", methods=["POST"])
def login_aluno():
    # Obtém os dados enviados pelo formulário de login (email e senha)
    email = request.form["email"]
    senha = request.form["senha"]

    # Estabelece a conexão com o banco de dados
    mydb = Conexao.conectar()
    mycursor = mydb.cursor()

    # Define a consulta SQL para buscar um aluno específico usando email e senha
    sql = "SELECT id_aluno FROM tb_alunos WHERE email = %s AND senha = %s"
    # Executa a consulta SQL com os parâmetros fornecidos
    mycursor.execute(sql, (email, senha))
    # Obtém o resultado da consulta (uma linha ou None)
    resultado = mycursor.fetchone()

    # Verifica se o resultado contém dados (ou seja, se as credenciais estão corretas)
    if resultado:
        # Se as credenciais forem válidas, armazena o ID do aluno na sessão
        session['id_aluno'] = resultado[0]
        # Redireciona para a página principal do aluno
        return redirect(url_for('pag-inicial.html'))
    else:
        # Se as credenciais forem inválidas, exibe uma mensagem de erro e reexibe o formulário de login
        flash("Credenciais inválidas")
        return render_template('login_aluno.html')

@app.route("/pagina-aluno")
def pagina_aluno():
    # Verifica se o ID do aluno está armazenado na sessão (se o aluno está autenticado)
    if 'id_aluno' not in session:
        # Se o ID do aluno não estiver na sessão, redireciona para a página de login
        return redirect(url_for('login_aluno'))
    # Se o aluno estiver autenticado, exibe uma mensagem de boas-vindas com o ID do aluno
    return "Bem-vindo à página do aluno, ID: " + session['id_aluno']

@app.route("/login-motorista", methods=["POST"])
def login_motorista():
    email = request.form["email"]
    senha = request.form["senha"]

    mydb = Conexao.conectar()
    mycursor = mydb.cursor()

    # Buscar o motorista pelo e-mail
    sql = "SELECT cpf, senha FROM tb_motoristas WHERE email = %s"
    mycursor.execute(sql, (email,))
    resultado = mycursor.fetchone()

    if resultado:
        cpf, senha_hash = resultado
        # Verificar a senha fornecida com o hash armazenado
        if bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8')):
            session['cpf_motorista'] = cpf
            return redirect(url_for('listar-aluno.html'))
        else:
            flash("Credenciais inválidas")
            return render_template('login_motorista.html')
    else:
        flash("Credenciais inválidas")
        return render_template('login_motorista.html')

@app.route("/pagina-motorista")
def pagina_motorista():
    if 'cpf_motorista' not in session:
        return redirect(url_for('login_motorista'))
    return "Bem-vindo à página do motorista, CPF: " + session['cpf_motorista']

@app.route("/listarAluno")
def pag_inicio():
    return render_template('listar-aluno.html')

app.run(debug=True)