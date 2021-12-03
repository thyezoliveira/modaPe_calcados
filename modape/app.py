from flask import Flask, render_template, request, redirect, session,url_for
from flask.helpers import url_for

app = Flask(__name__)
app.secret_key = '7a927480dcd9c2cd77caba2781b4aacd0f04fc4c683f0a9f4e39f94b1c00a170'
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
usuario2 = Usuario('admin', 'admin')
#------------------------------------X------------------------------------

# Rota da Tela de login --------------------------------------------------
@app.route('/', methods=['GET','POST'])
#@templated()
def index():
    style = url_for('static', filename='style.css')
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'], style=style)
    return render_template('index.html', style=style)
    # return dict(style=style)

#-----------------------------------X------------------------------------

# Rota da Area de autenticação -----------------------------------------
@app.route('/autenticacao', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    if username == usuario1.get_username():
        if password == usuario1.get_password():
            session['username'] = username
            return redirect(url_for('main'), code=307, Response=None)
        else:
            return "Senha incorreta!"
    elif username == usuario2.get_username():
        if password == usuario2.get_password():
            session['username'] = username
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
    return render_template('dashboard.html', username=session['username'], style=style)

# -----------------------------------X------------------------------------

# Rota de produtos -------------------------------------------------------
@app.route('/produtos', methods=['GET'])
def products():
    style = url_for('static', filename='style.css')
    return render_template('products.html', name=usuario1.get_username(), style=style)
# ------------------------------------------------------------------------

# Rota para Sair ------------------------------------------------------
@app.route('/sair', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'), code=307, Response=None)

# -----------------------------------X------------------------------------

# Ativar aplicação ao executar o arquivo----------------------------------
if __name__ == '__main__':
    app.run(debug=True)
#------------------------------------X------------------------------------