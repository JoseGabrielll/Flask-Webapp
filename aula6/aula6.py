#Objetivo: Fazer com que somente usuários logados possam criar um novo jogo, adicionar o url_for, melhorar o sistema de login
#Ate o momento existe 1 senha e qlq pessoa entra com essa senha, vamos add vários usuários cada um com sua senha

from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'gabriel'

#Por praticidade não estou usando nenhum encapsulamento das informações nas classes 
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

#Criar usuários que terão acesso para adicionar novos jogos
#Normalmente esses usuários estariam em BD's
user1 = Usuario('pepe', 'José Gabriel', '12345')
user2 = Usuario('felipe', 'Felipe Silva', '4321')
user3 = Usuario('ana', 'Ana Maria', 'anaana')

#Criando um dicionario de usuarios
usuarios = {user1.id: user1, 
            user2.id: user2, 
            user3.id: user3}

#Criar objetos e depois adicionar na lista de jogos
jogo1 = Jogo('Mario', 'Aventura', 'Nitendo')
jogo2 = Jogo('Ragnarok', 'RPG', 'PC')
lista_jogos = [jogo1, jogo2] #Lista de jogos que serão passados por parâmetro

@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Lista de Jogos', jogos=lista_jogos) #utilizando uma página HTML , 

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))   
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
    return redirect(url_for('index')) #redirecionando para o index

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():

    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pag = request.form['proxima']
            return redirect(proxima_pag)
        else:
            flash('Senha incorreta!! Tente novamente')
            return redirect(url_for('login'))
    else :
        flash('Usuário não está cadastrado!! Tente novamente')
        return redirect (url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário desconectado')
    return redirect(url_for('index'))

app.run()
#app.run(host='0.0.0.0', port=8080) - se quiser configurar manualmente o servidor e a porta 

'''
render_template() é um helper do flask que ajuda a renderizar o HTML
Ele basicamente envia as informações do .py para o .html (sintaxe do Jinja2)
'''