from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from usuario import Usuario
from pagamentos import Pagamentos
from conexao import Conexao
from upload_file import upload_file


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
            flash("Usuário cadastrado com sucesso!")
            return redirect('/logar')
        else:
            flash("Erro ao cadastrar o usuário. Tente novamente.")
            return redirect('/')

@app.route("/cadastrar-aluno", methods=['GET','POST'])
def pag_cadastro_aluno():
    if request.method == 'GET':
        return render_template('cadastro-aluno.html')
    else:
        nome_aluno = request.form["nome-aluno"] 
        escola = request.form["escola"]
        ano = request.form["ano"]
        foto_aluno = request.files["foto-aluno"]
        condicao_medica = request.form["condicao-medica"]
        nome_responsavel = request.form["nome-responsavel"]
        endereco_responsavel = request.form["endereco-aluno"]
        tel_responsavel = request.form["telefone-responsavel"]
        email_responsavel = request.form["email-aluno"]
        serie_aluno = request.form["serie-aluno"]

        link_foto = upload_file(foto_aluno)
        usuario = Usuario()
        if usuario.cadastrar_aluno(nome_aluno, link_foto, condicao_medica, escola, ano, nome_responsavel, endereco_responsavel, tel_responsavel, email_responsavel, serie_aluno):
            return redirect('/listar-alunos') 
        else:
           return redirect('/cadastrar-aluno')
    
@app.route("/cadastrar-aluno/<codigo>", methods=['GET','POST'])
def pag_cadastro_usuario(codigo):
    usuario = Usuario()
    verify_codigo = usuario.verficar_codigo(codigo)
    
    if verify_codigo == True:
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
            serie = request.form["serie-aluno"]

            link_foto = upload_file(foto_aluno)
            usuario = Usuario()
            if usuario.cadastrar_aluno(nome_aluno, link_foto, condicao_medica, escola, nome_responsavel, endereco_responsavel, tel_responsavel, email_responsavel, serie):
                return redirect('/listar-alunos') 
            else:
                return redirect('/cadastrar-aluno')
    else:
        return "ERROR"
        
@app.route("/gerar-codigo", methods=['GET'])
def formulario():
    usuario = Usuario
    link = usuario.gerar_codigo()
    return jsonify({"link": link}),200
                                              
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
            flash("alert('login ou senha incorretos!')")
            return redirect("/logar")

@app.route("/historico_pagamento", methods=['GET'])
def historico_pagamento():
    pagamentos = Pagamentos()
    historico = pagamentos.listar_historico()  # Chama o método listar_historico()

    # Renderiza o template com os pagamentos ou uma lista vazia
    return render_template("historico-pagamento.html", pagamentos=historico)

    
@app.route("/historico_pagamento_filtro", methods=['POST'])
def historico_pagamento_filtro():
    # Recupera o id do motorista logado a partir da sessão
    cpf_motorista = session["usuario_logado"]["cpf"]
    mes = request.form['mesPagamento']
    
    # Verifica se o motorista está logado
    if not cpf_motorista:
        return "Motorista não está logado", 401  # Retorna erro se não estiver logado

    pagamento = Pagamentos()
    
    # Obtém histórico de pagamentos feitos no mês
    historico_pagamentos = pagamento.listar_historico_filtro(mes, cpf_motorista)
    
    # Obtém lista de alunos sem pagamentos no mês
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
           # Pega os valores do formulário
        id_aluno = request.form.get("id_aluno")
        data_pagamento = request.form.get("data_pagamento")
        mes_pagamento = request.form.get("mes_pagamento")
        valor_pagamento = float(request.form["valor_pagamento"])
        cpf_motorista = session["usuario_logado"]["cpf"]


        # Instancia a classe Pagamentos e chama a função gerar_pagamento
    pagamento = Pagamentos()
    if pagamento.gerar_pagamento(id_aluno, mes_pagamento, data_pagamento, valor_pagamento, cpf_motorista):
        return redirect("/historico_pagamento")
    else:
        return "Erro ao gerar o pagamento", 500

     

@app.route("/quebra-contrato/<id_aluno>", methods=['GET'])
def quebra_foto(id_aluno):
    return render_template("quebra-contrato.html", id_aluno=id_aluno)

@app.route("/excluir-aluno/<id_aluno>", methods=['POST'])
def excluir_aluno(id_aluno):
    if request.method == 'GET':
        if 'usuario_logado' in session:
            usuario = Usuario()
            usuario.excluir_aluno(id_aluno)
            return redirect('/listar-alunos')




@app.route("/listar-alunos", methods=['GET', 'POST'])
def listar_alunos():
    usuario = Usuario()  # Inicializa a classe Usuario
    pesquisa = request.args.get("pesquisa-aluno")  # Obtém o parâmetro 'pesquisa-aluno' da URL

    if pesquisa:
        # Se uma pesquisa foi realizada, filtra os alunos pelo nome
        alunos_filtrados = usuario.listar_aluno_por_nome(pesquisa)  # Lista de alunos filtrados pelo nome
    else:
        # Se não houver pesquisa, lista todos os alunos
        alunos_filtrados = usuario.listar_contratos_motorista()  # Lista de todos os alunos

    # Independente de pesquisa, obtém a lista de todas as escolas disponíveis
    lista_completa_alunos = usuario.listar_contratos_motorista()  # Lista completa de todos os alunos
    escolas = {aluno['escola'] for aluno in lista_completa_alunos}  # Conjunto de todas as escolas (evita duplicatas)

    # Renderiza o template, passando os alunos filtrados e todas as escolas
    return render_template("listar-aluno.html", alunos=alunos_filtrados, escolas=escolas)


@app.route("/excluir-historico/<id_pagamento>", methods=['POST'])
def excluir_historico(id_pagamento):
    if 'usuario_logado' in session:
        usuario = Pagamentos()
        if usuario.excluir_historico(id_pagamento):
            flash("Pagamento excluído com sucesso!")
        else:
            flash("Erro ao excluir pagamento.")
        return redirect('/historico_pagamento')
    
@app.route('/editar-aluno/<int:id_aluno>', methods=['GET', 'POST'])
def editar_aluno(id_aluno):
    conn = Conexao.conectar()
    cursor = conn.cursor(dictionary=True)

    # Quando o método for GET, busque os dados do aluno para preencher o formulário
    if request.method == 'GET':
        cursor.execute("SELECT * FROM tb_alunos WHERE id_aluno = %s", (id_aluno,))
        aluno = cursor.fetchone()
        
        if aluno:
            return render_template('editar-aluno.html', aluno=aluno)
        else:
            return "Aluno não encontrado", 404

    # Quando o método for POST, salve os dados atualizados
    elif request.method == 'POST':
        nome_aluno = request.form.get('nome-aluno')
        condicao_medica = request.form.get('condicao-medica')
        escola = request.form.get('escola')
        nome_responsavel = request.form.get('nome-responsavel')
        endereco = request.form.get('endereco-aluno')
        telefone_responsavel = request.form.get('telefone-responsavel')
        email_responsavel = request.form.get('email-aluno')

        # Verificar se o usuário fez upload de uma nova foto
        foto_aluno = request.files.get('foto-aluno')
        if foto_aluno and foto_aluno.filename != '':
            # Validar tipo de arquivo de imagem
            if foto_aluno.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                foto_path = f"/static/images/{foto_aluno.filename}"
                foto_aluno.save(os.path.join('static', 'images', foto_aluno.filename))
            else:
                return "Formato de imagem inválido. Use PNG, JPG ou JPEG.", 400
        else:
            # Manter a foto existente
            cursor.execute("SELECT foto_aluno FROM tb_alunos WHERE id_aluno = %s", (id_aluno,))
            foto_path = cursor.fetchone()['foto_aluno']

        # Atualizar os dados do aluno no banco de dados
        cursor.execute("""
            UPDATE tb_alunos
            SET nome_aluno = %s, condicao_medica = %s, escola = %s, nome_responsavel = %s, endereco = %s, telefone_responsavel = %s, email_responsavel = %s, foto_aluno = %s
            WHERE id_aluno = %s
        """, (nome_aluno, condicao_medica, escola, nome_responsavel, endereco, telefone_responsavel, email_responsavel, foto_path, id_aluno))
        
        conn.commit()
        conn.close()

        return redirect('/listar-alunos')



    
if __name__ == "__main__":

    app.run(debug=True,host="0.0.0.0", port=8080)
