from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from usuario import Usuario
from pagamentos import Pagamentos
from conexao import Conexao
from upload_file import upload_file
import os

app = Flask(__name__)
app.secret_key = "banana"

@app.route("/")
def pag_inicio():
    return redirect('/logar')

@app.route("/pag-inicial-motorista")
def pag_inicial():
    return render_template("pag-inicial-motorista.html", session=session)

@app.route("/cadastrar-motorista", methods=['GET', 'POST'])
def pag_cadastro_motorista():
    if request.method == 'GET':
        return render_template('cadastro-motorista.html')
    else:
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        telefone = request.form["telefone"]
        email = request.form["email"]
        senha = request.form["senha"]

        usuario = Usuario()
        if usuario.cadastrar_motorista(nome, cpf, telefone, email, senha):
            flash("Usuário cadastrado com sucesso!", "success")
            return redirect('/logar')

        flash("Erro ao cadastrar motorista. Tente novamente.", "error")
        return redirect('/cadastrar-motorista')

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    return True

def validar_email(email):
    import re
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None


@app.route("/cadastrar-aluno", methods=['GET', 'POST'])
def pag_cadastro_aluno():
    if request.method == 'GET':
        return render_template('cadastro-aluno.html')
    else:
        nome_aluno = request.form["nome-aluno"]
        escola = request.form["escola"]
        foto_aluno = request.files["foto-aluno"]
        condicao_medica = request.form["condicao-medica"]
        nome_responsavel = request.form["nome-responsavel"]
        nome_responsavel2 = request.form["nome-responsavel2"]
        endereco_responsavel = request.form["endereco-aluno"]
        tel_responsavel = request.form["telefone-responsavel"]
        tel_responsavel2 = request.form["telefone-responsavel2"]
        serie_aluno = request.form["serie-aluno"]
        email_responsavel = request.form["email-aluno"]
        periodo = request.form["periodo-aluno"]

        link_foto = upload_file(foto_aluno)

        usuario = Usuario()
        if usuario.cadastrar_aluno(
            nome_aluno, link_foto, condicao_medica, escola,
            nome_responsavel, nome_responsavel2, endereco_responsavel,
            tel_responsavel, tel_responsavel2, email_responsavel,
            serie_aluno, periodo
        ):
            flash("Aluno cadastrado com sucesso!", "success")
            return redirect('/listar-alunos')
        else:
            flash("Erro ao cadastrar aluno. Tente novamente.", "error")
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
            flash("Login realizado com sucesso!", "success")
            return redirect('/pag-inicial-motorista')
        else:
            session.clear()
            flash("Login ou senha incorretos!", "error")
            return redirect("/logar")

@app.route("/historico_pagamento", methods=['GET'])
def historico_pagamento():
    pagamentos = Pagamentos()
    historico = pagamentos.listar_historico()
    return render_template("historico-pagamento.html", pagamentos=historico)

@app.route("/compontes")
def componente():
    return render_template("componente.html")
    
@app.route("/historico_pagamento_filtro", methods=['POST'])
def historico_pagamento_filtro():
    cpf_motorista = session["usuario_logado"]["cpf"]
    mes = request.form['mesPagamento']
    
    if not cpf_motorista:
        flash("Motorista não está logado.", "error")
        return "Motorista não está logado", 401

    pagamento = Pagamentos()
    historico_pagamentos = pagamento.listar_historico_filtro(mes, cpf_motorista)
    alunos_pendentes = pagamento.listar_alunos_pendentes(mes, cpf_motorista)
    
    return render_template("historico-pagamento.html", 
                           pagamentos=historico_pagamentos, 
                           alunos_pendentes=alunos_pendentes)

@app.route("/gerar-pagamento", methods=['GET', 'POST'])
def gerar_pagamento_get():
    if request.method == 'GET':
        usuario = Usuario()
        lista_alunos = usuario.listar_contratos_motorista()
        return render_template("gerar_pagamento.html", alunos=lista_alunos)
    else:
        id_aluno = request.form.get("id_aluno")
        data_pagamento = request.form.get("data_pagamento")
        mes_pagamento = request.form.get("mes_pagamento")
        valor_pagamento = float(request.form["valor_pagamento"])
        cpf_motorista = session.get("cpf_motorista")

        pagamento = Pagamentos()
        if pagamento.gerar_pagamento(id_aluno, mes_pagamento, data_pagamento, valor_pagamento, cpf_motorista):
            flash("Pagamento gerado com sucesso!", "success")
            return redirect("/historico_pagamento")
        else:
            flash("Erro ao gerar o pagamento.", "error")
            return redirect("/gerar-pagamento")

@app.route("/quebra-contrato/<id_aluno>", methods=['GET'])
def quebra_foto(id_aluno):
    return render_template("quebra-contrato.html", id_aluno=id_aluno)

@app.route("/excluir-aluno/<id_aluno>", methods=['GET', 'POST'])
def excluir_aluno(id_aluno):
    if request.method == 'GET':
        if 'usuario_logado' in session:
            usuario = Usuario()
            if usuario.excluir_aluno(id_aluno):
                flash("Aluno excluído com sucesso!", "success")
            else:
                flash("Erro ao excluir o aluno.", "error")
            return redirect('/listar-alunos')

@app.route("/listar-alunos", methods=['GET', 'POST'])
def listar_alunos():
    usuario = Usuario()
    pesquisa = request.args.get("pesquisa-aluno")

    if pesquisa:
        alunos_filtrados = usuario.listar_aluno_por_nome(pesquisa)
    else:
        alunos_filtrados = usuario.listar_contratos_motorista()

    lista_completa_alunos = usuario.listar_contratos_motorista()
    escolas = {aluno['escola'] for aluno in lista_completa_alunos}

    return render_template("listar-aluno.html", alunos=alunos_filtrados, escolas=escolas)

@app.route("/excluir-historico/<id_pagamento>", methods=['POST'])
def excluir_historico(id_pagamento):
    if 'usuario_logado' in session:
        usuario = Pagamentos()
        if usuario.excluir_historico(id_pagamento):
            flash("Pagamento excluído com sucesso!", "success")
        else:
            flash("Erro ao excluir pagamento.", "error")
        return redirect('/historico_pagamento')

@app.route('/editar-aluno/<int:id_aluno>', methods=['GET', 'POST'])
def editar_aluno(id_aluno):
    conn = Conexao.conectar()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'GET':
        cursor.execute("SELECT * FROM tb_alunos WHERE id_aluno = %s", (id_aluno,))
        aluno = cursor.fetchone()
        
        if aluno:
            return render_template('editar-aluno.html', aluno=aluno)
        else:
            flash("Aluno não encontrado.", "error")
            return redirect('/listar-alunos')

    elif request.method == 'POST':
        nome_aluno = request.form.get('nome-aluno')
        condicao_medica = request.form.get('condicao-medica')
        escola = request.form.get('escola')
        nome_responsavel = request.form.get('nome-responsavel')
        endereco = request.form.get('endereco-aluno')
        telefone_responsavel = request.form.get('telefone-responsavel')
        email_responsavel = request.form.get('email-aluno')

        foto_aluno = request.files.get('foto-aluno')
        if foto_aluno and foto_aluno.filename != '':
            if foto_aluno.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                foto_path = f"/static/images/{foto_aluno.filename}"
                foto_aluno.save(os.path.join('static', 'images', foto_aluno.filename))
            else:
                flash("Formato de imagem inválido. Use PNG, JPG ou JPEG.", "error")
                return redirect(f'/editar-aluno/{id_aluno}')
        else:
            cursor.execute("SELECT foto_aluno FROM tb_alunos WHERE id_aluno = %s", (id_aluno,))
            foto_path = cursor.fetchone()['foto_aluno']

        cursor.execute("""
            UPDATE tb_alunos
            SET nome_aluno = %s, condicao_medica = %s, escola = %s, nome_responsavel = %s, endereco = %s, telefone_responsavel = %s, email_responsavel = %s, foto_aluno = %s
            WHERE id_aluno = %s
        """, (nome_aluno, condicao_medica, escola, nome_responsavel, endereco, telefone_responsavel, email_responsavel, foto_path, id_aluno))
        
        conn.commit()
        conn.close()
        
        flash("Aluno atualizado com sucesso!", "success")
        return redirect('/listar-alunos')

app.run(debug=True)
