#Objetivo: Integrar um arquivo HTML ao flask

from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/lista')
def ola():
    #Criar objetos e depois adicionar na lista de jogos
    jogo1 = Jogo('Mario', 'Aventura', 'Nitendo')
    jogo2 = Jogo('Ragnarok', 'RPG', 'PC')
    lista_jogos = [jogo1, jogo2] #Lista de jogos que serão passados por parâmetro

    return render_template('lista.html', jogos=lista_jogos) #utilizando uma página HTML , 

app.run()
#app.run(host='0.0.0.0', port=8080) - se quiser configurar manualmente o servidor e a porta 

'''
render_template() é um helper do flask que ajuda a renderizar o HTML
Ele basicamente envia as informações do .py para o .html (sintaxe do Jinja2)
'''