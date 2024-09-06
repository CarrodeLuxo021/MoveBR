from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from conexao import Conexao


app = Flask(__name__)
app.secret_key = "banana"

@app.route("/")
def pag_inicio():
    return render_template('index.html')


@app.route("/cadastrar-motorista", methods=["GET"])
def pag_cadastro():
    return render_template('pag-motorista.html')


@app.route("/cadastrar-motorista", methods=["POST"])
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

    sql = f"""
    INSERT INTO tb_motoristas (nome, cpf, cnh, cnpj, cidade, endereco, m_periodos, tel_motorista, email, senha)
    VALUES ('{nome}', '{cpf}', '{cnh}', '{cnpj}', '{cidade}', '{endereco}', '{periodo}', '{telefone}', '{email}', '{senha}')
    """

    mycursor.execute(sql)    
    mydb.commit()
    return render_template('pag-aluno.html')

@app.route("/cadastrar-aluno", methods=["POST"])
def cadastrar_aluno():
    nome_aluno = request.form["nome_aluno"]
    endereco = request.form["endereco"]
    cidade = request.form["cidade"]
    idade = request.form["idade"]
    nome_responsavel = request.form["nome_responsavel"]
    tel_responsavel = request.form["tel_responsavel"]
    a_periodo = request.form["a_periodo"]
    
    mydb = Conexao.conectar()
    mycursor = mydb.cursor()

    sql = """
    INSERT INTO tb_alunos (nome_aluno, endereco, cidade, idade, nome_responsavel, tel_responsavel, a_periodo)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    valores = (nome_aluno, endereco, cidade, idade, nome_responsavel, tel_responsavel, a_periodo)

    mycursor.execute(sql, valores)
    mydb.commit()

    return render_template('pag-aluno.html')

app.run(debug=True)