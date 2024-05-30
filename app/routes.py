import this

from app import app
from flask import render_template
from flask import request
import json
import requests
link = "https://vitorti18n-default-rtdb.firebaseio.com/" #Conectando ao banco

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
@app.route('/crud')
def crud():
    return render_template('crud.html', titulo="CRUD", nome="Vitor Cavallini")

@app.route('/adm')
def adm():
    return render_template('adm.html', titulo="Administrador", nome="Vitor Cavallini")


@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        usuario      = request.form.get("usuario")
        senha        = request.form.get("senha")
        telefone     = request.form.get("telefone")
        idade        = request.form.get("idade")
        cep          = request.form.get("cep")
        dados        = {"usuario":usuario,"senha":senha,"telefone":telefone,"idade":idade,"cep":cep}
        requisicao   = requests.post(f'{link}/cadastrar/.json', data=json.dumps(dados))
        return 'Cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'
@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') #Solicitar os dados que estão no banco
        dicionario = requisicao.json()
        return dicionario

    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'

@app.route('/listarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') #Solicitar os dados que estão no banco
        dicionario = requisicao.json()
        idCadastro = {""}
        for codigo in dicionario:
            usuario = dicionario[codigo]['']
            if usuario == "Vitor Cavallini":
                idCadastro = codigo
        return idCadastro
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'



@app.route('/atualizar')
def atualizar():
    try:
        dados = {"nome": "Lucca"}#Parâmetro de atualização
        requisicao = requests.patch(f'{link}/cadastrar/-NySNSADmCFbENf0xj11/.json', data=json.dumps(dados))
        return "Atualzado com sucesso!"

    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastrar/-NySNSADmCFbENf0xj11/.json')
        return "Excluido com sucesso!"
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'











