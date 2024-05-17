from app import app
from flask import render_template

@app.route('/') #Configurando uma rota web
@app.route('/index')
def index():
    return render_template('index.html', titulo="Página Inicial", nome="Vitor Cavallini")

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo="Sobre", nome="Vitor Cavallini")

@app.route('/login')
def login():
    return render_template('login.html', titulo="Login", nome="Vitor Cavallini")
@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo="Cadastro", nome="Vitor Cavallini")

@app.route('/palmeiras')
def palmeiras():
    return render_template('palmeiras.html', titulo="Palmeiras", nome="Vitor Cavallini")

@app.route('/real')
def real():
    return render_template('real.html', titulo="Real Madrid", nome="Vitor Cavallini")

@app.route('/vasco')
def vasco():
    return render_template('vasco.html', titulo="Vasco da Gama", nome="Vitor Cavallini")
