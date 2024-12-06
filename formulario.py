from usuario import Usuario
from flask import jsonify, Flask

app = Flask(__name__)
app.secret_key = "banana"


@app.route("/gerar-codigo", methods=['GET'])
def formulario():
    usuario = Usuario
    link = usuario.gerar_codigo()
    return jsonify({"link": link}),200