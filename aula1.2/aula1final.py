#Objetivo: Integrar um arquivo HTML ao flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/lista')
def ola():
    lista_jogos = ['Mario', 'CSGO', 'Pokemon', 'LoL'] #Lista de jogos que serão passados por parâmetro
    linkgoogle = 'https://www.google.com.br/' #Passando links pelo render_template
    return render_template('lista.html', jogos=lista_jogos, link=linkgoogle) #utilizando uma página HTML , 

app.run()
#app.run(host='0.0.0.0', port=8080) - se quiser configurar manualmente o servidor e a porta 

'''
render_template() é um helper do flask que ajuda a renderizar o HTML
Ele basicamente envia as informações do .py para o .html (sintaxe do Jinja2)
'''