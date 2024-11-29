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

@app.route("/cadastrar-aluno", methods=['GET', 'POST'])
def pag_cadastro_aluno():
    if request.method == 'GET':
        return render_template('cadastro-aluno.html')
    else:
        # Coleta de dados do formulário
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

        # Fazer o upload da foto e obter o link
        link_foto = upload_file(foto_aluno)

        # Instanciar o objeto Usuario
        usuario = Usuario()
        if usuario.cadastrar_aluno(
            nome_aluno, link_foto, condicao_medica, escola,
            nome_responsavel, nome_responsavel2, endereco_responsavel,
            tel_responsavel, tel_responsavel2, email_responsavel,
            serie_aluno, periodo
        ):
            return redirect('/listar-alunos')
        else:
            return redirect('/cadastrar-aluno')

@app.route("/cadastrar-aluno/<codigo>", methods=['GET','POST'])
def pag_cadastro_usuario(codigo):
    usuario = Usuario()
    verify_codigo = usuario.verificar_codigo(codigo)
    
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
                flash("alert('cadastro efetuado com sucesso')")
                return render_template('check-cadastro.html')
            else:
                return redirect(f'/cadastrar-aluno/{codigo}')
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
    # Recupera o CPF do motorista logado a partir da sessão
    cpf_motorista = session.get("usuario_logado", {}).get("cpf")
    
    # Verifica se o motorista está logado
    if not cpf_motorista:
        return "Motorista não está logado", 401  # Retorna erro se não estiver logado

    mes = request.form.get('mesPagamento')  # Usar 'get' para evitar KeyError

    pagamento = Pagamentos()

    # Se o mês foi fornecido, filtra os pagamentos e alunos pendentes por mês
    if mes:
        historico_pagamentos = pagamento.listar_historico_filtro(mes, cpf_motorista)
        alunos_pendentes = pagamento.listar_alunos_pendentes(mes, cpf_motorista)
    else:
        # Caso não tenha sido fornecido mês, busca todos os pagamentos
        historico_pagamentos = pagamento.listar_historico_filtro(None, cpf_motorista)
        alunos_pendentes = pagamento.listar_alunos_pendentes(None, cpf_motorista)
    
    return render_template("historico-pagamento.html", 
                           pagamentos=historico_pagamentos, 
                           alunos_pendentes=alunos_pendentes)



@app.route("/listar_historico_aluno/<int:id_aluno>", methods=['GET'])
def listar_historico_aluno(id_aluno):
    try:
        # Conectando ao banco de dados
        mydb = Conexao.conectar()
        mycursor = mydb.cursor()

        # Consulta SQL para listar os pagamentos do aluno específico
        sql = """
        SELECT nome_aluno, metodo_pagamento, data_pagamento, valor_pagamento, id_pagamento 
        FROM historico_pagamentos 
        WHERE id_aluno = %s;
        """
        mycursor.execute(sql, (id_aluno,))
        resultados = mycursor.fetchall()

        # Organizando os dados em uma lista de dicionários
        pagamentos = [{
            "nome_aluno": linha[0],
            "metodo_pagamento": linha[1],
            "data_pagamento": linha[2],
            "valor_pagamento": linha[3],
            "id_pagamento": linha[4],
        } for linha in resultados]

        mydb.close()

        # Renderizando o template de histórico de pagamentos para o aluno
        return render_template("historico-pagamento.html", pagamentos=pagamentos, id_aluno=id_aluno)

    except Exception as e:
        print(f"Erro ao listar pagamentos do aluno {id_aluno}: {e}")
        return "Erro ao listar pagamentos do aluno", 500

@app.route("/gerar-pagamento", methods=['GET', 'POST'])
def gerar_pagamento_get():
    if request.method == 'GET':
        usuario = Usuario()
        lista_alunos = usuario.listar_contratos_motorista()
        return render_template("gerar_pagamento.html", alunos=lista_alunos)
    else:
        # Pega os valores do formulário
        id_aluno = request.form.get("id_aluno")
        nome_aluno = request.form.get("nome_aluno")
        data_pagamento = request.form.get("data_pagamento")
        mes_pagamento = request.form.get("mes_pagamento")
        valor_pagamento = float(request.form["valor_pagamento"])
        metodo_pagamento = request.form.get("metodo_pagamento")  # Novo campo
        cpf_motorista = session["usuario_logado"]["cpf"]

        # Instancia a classe Pagamentos e chama a função gerar_pagamento
        pagamento = Pagamentos()
        if pagamento.gerar_pagamento(id_aluno, nome_aluno, mes_pagamento, data_pagamento, valor_pagamento, metodo_pagamento, cpf_motorista):
            return redirect("/historico_pagamento")
        else:
            return "Erro ao gerar o pagamento", 500

     

@app.route("/quebra-contrato/<id_aluno>", methods=['GET'])
def quebra_foto(id_aluno):
    return render_template("quebra-contrato.html", id_aluno=id_aluno)

@app.route("/excluir-aluno/<id_aluno>", methods=['GET', 'POST'])
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


@app.route("/excluir-historico/<int:id_pagamento>", methods=['POST'])
def excluir_historico(id_pagamento):
    if 'usuario_logado' in session:
        usuario = Pagamentos()
        if usuario.excluir_historico(id_pagamento):
            flash("Pagamento excluído com sucesso!")
        else:
            flash("Erro ao excluir pagamento.")
        return redirect(url_for('historico_pagamento'))  # Redireciona de volta para a página de histórico de pagamentos.

    # Se o usuário não estiver logado, redireciona para o login
    flash("Você precisa estar logado para excluir pagamentos.")
    return redirect(url_for('/logar'))


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



    

app.run(debug=True)
