
from flask import Flask,render_template,request
app = Flask(__name__)

import datetime

@app.route('/')
def home():
    return render_template('esercizio2.html')

@app.route('/login2', methods = ['GET'])
def login():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    sesso = request.args.get('sesso')
    if sesso == "uomo" :
        saluto = "benvenuto"
    else:
        saluto = "benvenuta"
    return render_template('saluto.html',saluto = saluto,nome=nome)

@app.route('/MassaCorporea', methods = ['GET'])
def MassaCorporea():
    peso = float(request.args.get("peso"))
    altezza = float(request.args.get("altezza")) / 100
    
    IMC = int(peso/(altezza ** 2))
    if IMC <= 19:
        risultato = "sei sottopeso rafy"
    elif IMC > 19 and IMC < 25:
        risultato = "sei normale rafy"
    elif IMC >= 25:
        risultato = "sei obeso rafy"
    return render_template('risultato.html',risultato = risultato, IMC = IMC)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)