from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from usuario import Usuario
from pagamentos import Pagamentos
from upload_file import upload_file

app = Flask(__name__)
app.secret_key = "banana"

@app.route("/")
def pag_inicio():
    return redirect('/logar')

@app.route("/pag-inicial-motorista")
def pag_inicial():
    return render_template("pag-inicial-motorista.html", session=session)

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
        flash("alert('Usuário cadastrado com sucesso!')")

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
            return redirect('/listar-alunos') 
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
            return redirect('/pag-inicial-motorista')
        else:
            session.clear()
            return redirect("/logar")
    


@app.route("/listar-alunos", methods=['GET', 'POST'])
def listar_alunos():
    if request.method == 'GET':
        usuario = Usuario()
        lista_alunos = usuario.listar_aluno()
        return render_template("listar-aluno.html", alunos=lista_alunos)


@app.route("/historico_pagamento", methods=['GET'])
def historico_pagamento():
    if request.method == 'GET':
        pagamentos = Pagamentos()
        historico = pagamentos.listar_historico()  # Chama o método listar_historico()

        # Instancia a classe Pagamentos e chama a função gerar_pagamento
    pagamento = Pagamentos()
    if pagamento.gerar_pagamento(id_aluno, mes_pagamento, data_pagamento, valor_pagamento):
        return render_template("historico-pagamento.html")
    if historico:
        return render_template("historico-pagamento.html", pagamentos=historico)  # Passa a lista de pagamentos
    else:
        return render_template("historico-pagamento.html", pagamentos=[])
        if historico:
            return render_template("historico-pagamento.html", pagamentos=historico)  # Passa a lista de pagamentos
        else:
            return render_template("historico-pagamento.html", pagamentos=[])



@app.route("/historico_pagamento_filtro/<mes>", methods=['post'])
def historico_pagamento_filtro(mes):
    mes = request.args.get('mes')
     # Recupera o id do motorista logado a partir da sessão
    cpf_motorista = session.get("cpf_motorista")
    
    # Verifica se o motorista está logado
    if not cpf_motorista:
        return "Motorista não está logado", 401  # Retorna erro se não estiver logado

    pagamento = Pagamentos()
    if pagamento.gerar_pagamento(mes, cpf_motorista):
        return render_template("historico_pagamento.html")
    else:
        return "Erro ao gerar pagamento", 500

@app.route("/gerar-pagamento", methods=['GET'])
def gerar_pagamento_get():
    usuario = Usuario()
    lista_alunos = usuario.listar_aluno()
    return render_template("gerar_pagamento.html", alunos=lista_alunos)


@app.route("/gerar-pagamento", methods=['POST'])
def gerar_pagamento_post():
    try:
        # Pega os valores do formulário
        id_aluno = request.form["id_aluno"]
        data_pagamento = request.form["data_pagamento"]
        mes_pagamento = request.form["mes_pagamento"]
        valor_pagamento = float(request.form["valor_pagamento"])
        cpf_motorista = session.get("cpf_motorista")  # Certifique-se de que o motorista esteja logado

        # Instancia a classe Pagamentos e chama a função gerar_pagamento
        pagamento = Pagamentos()
        if pagamento.gerar_pagamento(id_aluno, mes_pagamento, data_pagamento, valor_pagamento, cpf_motorista):
            return redirect("/historico_pagamento")  # Redireciona para o histórico de pagamentos após sucesso
        else:
            return "Erro ao gerar o pagamento", 500  # Retorna erro no caso de falha
    except Exception as e:
        print(f"Erro: {e}")
        return "Erro no processamento", 500

    
@app.route("/quebra-contrato/<id_aluno>", methods=['GET'])
def quebra_foto(id_aluno):
    return render_template("quebra-contrato.html", id_aluno = id_aluno)
    
@app.route("/excluir-aluno/<id_aluno>", methods=['GET', 'POST'])
def excluir_aluno(id_aluno):
    if request.method == 'GET':
        if 'usuario_logado' in session:
            usuario = Usuario()
            usuario.excluir_aluno(id_aluno)
            return redirect('/listar-alunos')
    
app.run(debug=True)