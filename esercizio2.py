
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
    peso = request.args.get("peso")
    altezza = request.args.get("altezza")
    IMC = peso/(altezza * altezza)
    if IMC <= 19:
        print("sei sottopeso rafy")
    elif IMC > 19 & IMC <= 25  :
        print("sei normale rafy")
    elif IMC >= 30:
        print("sei obeso rafy")
    return render_template('risultato.html',IMC= IMC)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)