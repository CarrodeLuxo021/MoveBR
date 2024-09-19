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
    
    # Criação da instância da classe Usuario
    usuario = Usuario()
    
    # Chama a função cadastrar_motorista
    if usuario.cadastrar_motorista(nome, endereco, cidade, cpf, cnh, cnpj, telefone, email, senha):
        return render_template('pag-inicial.html')
    else:
        return "Erro ao cadastrar motorista", 500


@app.route("/cadastrar-responsavel", methods=["POST"])
def cadastrar_resp():
    nome_responsavel = request.form["nome_responsavel"]
    endereco_responsavel = request.form["endereco_responsavel"]
    tel_responsavel = request.form["tel_responsavel"]
    cpf_responsavel = request.form["cpf_responsavel"]
    email_responsavel = request.form["email_responsavel"]
    senha_responsavel = request.form["senha_responsavel"]

    # Conectar ao banco de dados
    
    usuario = Usuario()
    
    if usuario.cadastrar_responsavel(nome_responsavel, endereco_responsavel, tel_responsavel, cpf_responsavel, email_responsavel, senha_responsavel):
        return render_template('pag-inicial.html')
    else:
        return 'ERRO AO CADASTRAR'

@app.route("/cadastrar-aluno", methods=["POST"])
def cadastrar_aluno():
    nome_aluno = request.form["nome_aluno"]
    condicao_medica = request.form.get("condicao_medica")  # Pode ser opcional
    idade = request.form["idade"]

    # Criação da instância da classe Usuario
    usuario = Usuario()
    
    # Chama a função cadastrar_aluno
    if usuario.cadastrar_aluno(nome_aluno, condicao_medica, idade):
        return render_template('pag-inicial.html')
    else:
        return "Erro ao cadastrar aluno", 500

    

@app.route("/login-responsavel", methods=["POST"])
def login_responsavel():
    # Obtém os dados enviados pelo formulário de login (email e senha)
    email = request.form["email"]
    senha = request.form["senha"]

    usuario = Usuario()
    
    # Chama a função cadastrar_aluno
    if usuario.logar_resposavel(email, senha):
        return render_template('pag-inicial.html')
    else:
        return "Erro ao cadastrar aluno", 500



@app.route("/login-motorista", methods=["POST"])
def login_motorista():
    email = request.form["email"]
    senha = request.form["senha"]

    usuario = Usuario()
    
    # Chama a função cadastrar_aluno
    if usuario.logar_motorista(email, senha):
        return render_template('pag-inicial.html')
    else:
        return "Erro ao cadastrar aluno", 500
    
    

@app.route("/pagina-motorista")
def pagina_motorista():
    if 'cpf_motorista' not in session:
        return redirect(url_for('login_motorista'))
    return "Bem-vindo à página do motorista, CPF: " + session['cpf_motorista']


app.run(debug=True)