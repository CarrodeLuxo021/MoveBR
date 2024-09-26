from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from usuario import Usuario

app = Flask(__name__)
app.secret_key = "banana"

@app.route("/")
def pag_inicio():
    return render_template('index.html')

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
        cidade = request.form["cidade"]
        endereco = request.form["endereço"]
        foto_motorista = request.form["ft_motorista"]
        foto_van = request.form["ft_veiculo"]
        valor_mensalidade = request.form["valor_cobrado"]

        usuario = Usuario()
        if usuario.cadastrar_motorista(nome, cpf, cnh, cnpj, telefone, email, senha, cidade, endereco, foto_motorista, foto_van, valor_mensalidade):
            return render_template('') 
        
        else:
            return 'ERRO AO CADASTRAR'
        
        

@app.route("/cadastrar-aluno", methods=['GET','POST'])
def pag_cdaluno():
    if request.method == 'GET':
        return render_template('cadastro-aluno.html')
    else:
        nome_aluno = request.form["nomeAluno"]
        escola = request.form["escola"]
        foto_aluno = request.form["ft_aluno"]
        condicao_medica = request.form["condicao_medica"]
        nome_responsavel = request.form["nomeResponsavel"]
        cpf_responsavel = request.form["cpfResponsavel"]
        endereco_responsavel = request.form["endereço"]
        tel_responsavel = request.form["telefoneResponsavel"]
        email_responsavel = request.form["emailAluno"]
        senha_responsavel = request.form["senhaAluno"]

        usuario = Usuario()
        if usuario.cadastrar_aluno(nome_aluno, foto_aluno, condicao_medica, escola, nome_responsavel, cpf_responsavel, endereco_responsavel, tel_responsavel, email_responsavel, senha_responsavel):
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