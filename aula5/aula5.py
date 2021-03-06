#Objetivo: Criar uma tela de login, autenticar usuarios

from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'gabriel'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

#Criar objetos e depois adicionar na lista de jogos
jogo1 = Jogo('Mario', 'Aventura', 'Nitendo')
jogo2 = Jogo('Ragnarok', 'RPG', 'PC')
lista_jogos = [jogo1, jogo2] #Lista de jogos que serão passados por parâmetro

@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Lista de Jogos', jogos=lista_jogos) #utilizando uma página HTML , 

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

#Por padrão é o get, porém vamos alterar para o POST:
@app.route('/criar', methods=['POST',]) #Trata o dado que ta chegando do formulário (trata o request)
def criar(): 
    #Quando recebo o jogo novo eu devo adicionar ele na lista
    #Recupera as informações pelo request através do 'name' do fomrulário
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    novo_jogo = Jogo(nome, categoria, console)
    lista_jogos.append(novo_jogo)
    return redirect('/') #redirecionando para o index

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso')
        return redirect('/')
    else :
        flash('Senha incorreta!! Tente novamente')
        return redirect ('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário desconectado')
    return redirect('/')

app.run()
#app.run(host='0.0.0.0', port=8080) - se quiser configurar manualmente o servidor e a porta 

'''
render_template() é um helper do flask que ajuda a renderizar o HTML
Ele basicamente envia as informações do .py para o .html (sintaxe do Jinja2)
'''