""" from flask import Flask, request, render_template
from usuario import Usuario


app = Flask(__name__)


@app.route("/listarAlunos", methods = ['GET', 'POST'])
def listarAlunos():
    if request.method == 'GET':
        return render_template("listarAlunos.html")
    else: """

from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from usuario import Usuario




app = Flask(__name__)
app.secret_key = "banana"

@app.route("/")
def pag_inicio():
    return render_template('index.html')


@app.route("/cadastrar-motorista", methods=['GET','POST'])
def pag_cadastro():
    if request.method == 'GET':
        return render_template('pag-motorista.html')
    else:
        nome = request.form["name"]
        cpf = request.form["cpf"]
        cnpj = request.form["cnpj"]
        cnh = request.form["cnh"]
        telefone = request.form["phone"]
        email = request.form["email"]
        senha = request.form["senha"]
        cidade = request.form["cidade"]

        usuario = Usuario()
        if usuario.cadastrar(nome, cpf, cnpj, cnh, telefone, email, senha, cidade):
            return 'CADASTRO COM SUCESSO'
        else:
            return 'ERRO AO CADASTRAR'

@app.route("/cadastrar-aluno", methods=['GET','POST'])
def pag_cdaluno():
    if request.method == 'GET':
        return render_template('pag-aluno.html')
    else: 
        
        nome_aluno = request.form["nome_aluno"]
        endereco = request.form["endereco"]
        cidade = request.form["cidade"]
        idade = request.form["idade"]
        nome_responsavel = request.form["nome_responsavel"]
        tel_responsavel = request.form["tel_responsavel"]

        usuario = Usuario()
        if usuario.cadastrar_aluno(nome_aluno, endereco, cidade, idade, nome_responsavel, tel_responsavel):
            return 'ALUNO CADASTRADO COM SUCESSO'
        else:
            return 'ERRO AO CADASTRAR'
        
@app.route("/logar", methods=['GET', 'POST'])
def logar():
    if request.method == 'GET':
        return render_template("logar.html")
    else:
        senha = request.form['senha']
        email = request.form['email']
        usuario = Usuario()
        usuario.logar(senha, email)
        if usuario.logado == True:
            session['usuario_logado'] = {"nome": usuario.nome,
                                         "email": usuario.email,
                                         "cpf": usuario.cpf}
            return render_template("pag-motorista.html")
        else:
            session.clear()
            return redirect("/logar")

@app.route("/listar-motorista", methods=['GET', 'POST'])
def listar_motorista():
    if request.method == 'GET':
        return render_template("listar-aluno.html")
    else:
        usuario = Usuario()
        usuario.listar_usuario()
    

app.run(debug=True)

    