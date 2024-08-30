from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from conexao import Conexao


app = Flask(__name__)
app.secret_key = "banana"

@app.route("/")
def pag_inicio():
    return render_template('index.html')


@app.route("/cadastrar", methods=["GET"])
def pag_cadastro():
    return render_template('cadastro.html')


@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    nome = request.form["nome"]
    cpf = request.form["cpf"]
    cnpj = request.form["cnpj"]
    cnh = request.form["cnh"]
    periodo = request.form["periodo"]
    telefone = request.form["telefone"]
    email = request.form["email"]
    senha = request.form["senha"]
    cidade = request.form["cidade"]
    endereco = request.form["endereco"]
    

    mydb = Conexao.conectar()

    mycursor = mydb.cursor()

    sql = "INSERT INTO tb_motoristas (nome, cpf, cnh, cnpj, cidade, endereco, m_periodos, tel_motorista, email, senha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (nome, cpf, cnh, cnpj, cidade, endereco, periodo, telefone, email, senha)

    mycursor.execute(sql, valores)    
    mydb.commit()
    
    return render_template('login.html')


app.run(debug=True)