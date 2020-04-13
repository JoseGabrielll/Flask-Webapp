#Onjetivo: Criar um primeiro programa flask que será mostrado no endereço padrão
from flask import Flask

app = Flask(__name__)

@app.route('/inicio') #ficará no link/inicio
def ola():
    return 'Eu sou o início'

app.run()