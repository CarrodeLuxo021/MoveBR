from flask import Flask, request, render_template
from usuario import Usuario


app = Flask(__name__)


@app.route("/listarAlunos", methods = ['GET', 'POST'])
def listarAlunos():
    if request.method == 'GET':
        return render_template("listarAlunos.html")
    else:

    