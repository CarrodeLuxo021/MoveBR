from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from usuario import Usuario

app = Flask(__name__)
app.secret_key = "banana"

@app.route("/")
def pag_inicio():
    return render_template('pag-inicial.html')

@app.route("/cadastrar-motorista", methods=['GET','POST'])
def pag_cadastro_motorista():
    if request.method == 'GET':
        return render_template('cadastro-motorista.html')
    else:
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        cnpj = request.form["cnpj"]
        cnh = request.form["cnh"]
        telefone = request.form["telefone"]
        email = request.form["email"]
        senha = request.form["senha"]


        usuario = Usuario()
        if usuario.cadastrar_motorista(nome, cpf, cnpj, cnh, telefone, email, senha):
            return render_template('login-motorista.html') 
        
        else:
            return render_template('cadastro-motorista.html')
        
        

@app.route("/cadastrar-aluno", methods=['GET','POST'])
def pag_cadastro_aluno():
    if request.method == 'GET':
        return render_template('cadastro-aluno.html')
    else:
        nome_aluno = request.form["nome-aluno"]
        escola = request.form["escola"]
        foto_aluno = request.form["foto-aluno"]
        condicao_medica = request.form["condicao-medica"]
        nome_responsavel = request.form["nome-responsavel"]
        endereco_responsavel = request.form["endereco-aluno"]
        tel_responsavel = request.form["telefone-responsavel"]
        email_responsavel = request.form["email-aluno"]

        usuario = Usuario()
        if usuario.cadastrar_aluno(nome_aluno, foto_aluno, condicao_medica, escola, nome_responsavel, endereco_responsavel, tel_responsavel, email_responsavel):
             return render_template('pag-inicial-motorista.html') 
        else:
           return render_template('cadastro-aluno.html')
    

@app.route("/logar", methods=['POST', 'GET'])
def logar():
    if request.method == 'GET':
        return render_template("login-motorista.html")
    else:
        senha = request.form['senha']
        email = request.form['email']
        usuario = Usuario()
        if usuario.logar(email, senha):
            session['usuario_logado'] = {
                "nome": usuario.nome,
                "email": usuario.email,
                "cpf": usuario.cpf
            }
            return render_template("pag-inicial-motorista.html")
        else:
            session.clear()
            return redirect("/logar")

@app.route("/listar-motorista", methods=['GET', 'POST'])
def listar_motorista():
    if request.method == 'GET':
        usuario = Usuario()
        lista_usuarios = usuario.listar_usuario()
        return render_template("listar-motorista.html", usuarios=lista_usuarios)

@app.route("/listar-alunos", methods=['GET', 'POST'])
def listar_alunos():
    if request.method == 'GET':
        usuario = Usuario()
        lista_alunos = usuario.listar_aluno()
        return render_template("listar-aluno.html", alunos=lista_alunos)

app.run(debug=True)