from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from usuario import Usuario
from pagamentos import Pagamentos
from upload_file import upload_file

app = Flask(__name__)
app.secret_key = "banana"

@app.route("/")
def pag_inicio():
    return redirect('/logar')

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
            return redirect('/logar') 
        else:
            return redirect('/')
        
        
@app.route("/cadastrar-aluno", methods=['GET','POST'])
def pag_cadastro_aluno():
    if request.method == 'GET':
        return render_template('cadastro-aluno.html')
    else:
        nome_aluno = request.form["nome-aluno"] 
        escola = request.form["escola"]
        foto_aluno = request.files["foto-aluno"]
        condicao_medica = request.form["condicao-medica"]
        nome_responsavel = request.form["nome-responsavel"]
        endereco_responsavel = request.form["endereco-aluno"]
        tel_responsavel = request.form["telefone-responsavel"]
        email_responsavel = request.form["email-aluno"]

        link_foto = upload_file(foto_aluno)
        usuario = Usuario()
        if usuario.cadastrar_aluno(nome_aluno, link_foto, condicao_medica, escola, nome_responsavel, endereco_responsavel, tel_responsavel, email_responsavel):
             return redirect('/') 
        else:
           return redirect('/cadastrar-aluno')
        
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
            return render_template('pag-inicial-motorista.html', session=session)
        else:
            session.clear()
            return redirect("/logar")
            


@app.route("/listar-alunos", methods=['GET', 'POST'])
def listar_alunos():
    if request.method == 'GET':
        usuario = Usuario()
        lista_alunos = usuario.listar_aluno()
        return render_template("listar-aluno.html", alunos=lista_alunos)


@app.route("/gerar_pagamento", methods=['GET'])
def gerar_pagamento_get():
    usuario = Usuario()
    lista_alunos = usuario.listar_aluno()
    return render_template("gerar_pagamento.html", alunos=lista_alunos)

@app.route("/gerar_pagamento", methods=['POST'])
def gerar_pagamento_post():
    id_aluno = request.values["id_aluno"]
    data = request.form["data"]
    mes = request.form["mes"]
    valor = request.form["valor"]

    # Recupera o id do motorista logado a partir da sessão
    id_motorista = session.get("id_motorista")
    
    # Verifica se o motorista está logado
    if not id_motorista:
        return "Motorista não está logado", 401  # Retorna erro se não estiver logado

    pagamento = Pagamentos()
    if pagamento.gerar_pagamento(id_aluno, data, mes, valor, id_motorista):
        return render_template("historico_pagamento.html")
    else:
        return "Erro ao gerar pagamento", 500

app.run(debug=True)