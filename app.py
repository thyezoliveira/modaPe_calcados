from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import url_for

app = Flask(__name__)

# classe de usuário -----------------------------------------------------
class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

usuario1 = Usuario('modape', 'calcados2022')
#------------------------------------X------------------------------------

# Rota da Tela de login --------------------------------------------------
@app.route('/', methods=['GET'])
def index():
    style = url_for('static', filename='style.css')
    return render_template('index.html', style=style)

#-----------------------------------X------------------------------------

# Rota da Area de autenticação -----------------------------------------
@app.route('/autenticacao', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    if username == usuario1.get_username():
        if password == usuario1.get_password():

            return redirect(url_for('main'), code=307, Response=None)
        else:
            return "Senha incorreta!"
    else:
        return "Suas credenciais não são compativeis."

#------------------------------------X------------------------------------

# Rota do Dashboard ------------------------------------------------------
@app.route('/dashboard', methods=['POST'])
def main():
    style = url_for('static', filename='style.css')
    return render_template('dashboard.html', name=usuario1.get_username(), style=style)

# -----------------------------------X------------------------------------

# Rota de produtos -------------------------------------------------------
@app.route('/produtos', methods=['GET'])
def products():
    style = url_for('static', filename='style.css')
    return render_template('products.html', name=usuario1.get_username(), style=style)
# ------------------------------------------------------------------------

# Ativar aplicação ao executar o arquivo----------------------------------
if __name__ == '__main__':
    app.run(debug=True)
#------------------------------------X------------------------------------