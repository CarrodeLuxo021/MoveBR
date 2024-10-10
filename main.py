from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from usuario import Usuario
from pagamentos import Pagamentos

app = Flask(__name__)
app.secret_key = "banana"

@app.route("/")
def pag_inicio():
    return render_template('pag-inicial-motorista.html')

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
        foto_aluno = request.form["foto-aluno"]
        condicao_medica = request.form["condicao-medica"]
        nome_responsavel = request.form["nome-responsavel"]
        endereco_responsavel = request.form["endereco-aluno"]
        tel_responsavel = request.form["telefone-responsavel"]
        email_responsavel = request.form["email-aluno"]

        usuario = Usuario()
        if usuario.cadastrar_aluno(nome_aluno, foto_aluno, condicao_medica, escola, nome_responsavel, endereco_responsavel, tel_responsavel, email_responsavel):
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
            return redirect("/")
        else:
            session.clear()
            return redirect("/logar")
            


@app.route("/listar-alunos", methods=['GET', 'POST'])
def listar_alunos():
    if request.method == 'GET':
        if 'usuario_logado' in  session:
            usuario = Usuario()
            query = request.args.get('query')
            if query:
                lista_alunos = usuario.pesquisar_aluno(query)
            else:
                lista_alunos = usuario.listar_aluno()

            return render_template("listar-aluno.html", alunos=lista_alunos)
        else:
            return redirect('/logar')

@app.route("/gerar_pagamento", methods=['POST'])
def gerar_pagamento():
    id_aluno = request.form["id_aluno"]
    data = request.form["data"]
    mes = request.form["mes"]
    valor = request.form["valor"]
    pagamento = Pagamentos()
    if pagamento.gerar_pagamento(id_aluno, data, mes, valor):
        return render_template("gerar_pagamento.html")
    




@app.route("/excluir-aluno/<id_aluno>", methods=['GET', 'POST'])
def excluir_aluno(id_aluno):
    if request.method == 'GET':
        if 'usuario_logado' in session:
            usuario = Usuario()
            usuario.excluir_aluno(id_aluno)
            return redirect('/listar-alunos')
        
@app.route("/quebra-contrato/<id_aluno>", methods=['GET'])
def quebra_foto(id_aluno):
    return render_template("quebra-contrato.html", id_aluno = id_aluno)

@app.route("/historico_pagamento", methods=['GET'])
def historico_pagamento():
    return render_template("historico-pagamento.html")

@app.route("/historico_pagamento/<mes>", methods=['post'])
def historico_pagamento_filtro(mes):
    mes = request.args.get('mes')
     # Recupera o id do motorista logado a partir da sessão
    cpf_motorista = session.get("cpf_motorista")
    
    # Verifica se o motorista está logado
    if not cpf_motorista:
        return "Motorista não está logado", 401  # Retorna erro se não estiver logado
    
    pagamento = Pagamentos()
    if pagamento.listar_historico(mes, cpf_motorista):
        return render_template("historico-pagamento.html", )


app.run(debug=True)