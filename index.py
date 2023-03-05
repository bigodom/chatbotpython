from flask import Flask, render_template, request
from main import *

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/receber_string', methods=['GET', 'POST'])
def receber_string():
    
    string_digitada = request.args.get('string_digitada')
     
    string_resposta = responder_bot(string_digitada)
    
    return render_template('index.html', string_digitada=string_digitada, string_resposta=string_resposta)

@app.route('/corrigir_string', methods=['GET', 'POST'])
def corrigir_string():

    string_digitada = request.args.get('string_digitada')

    string_corrigida = request.args.get('string_corrigida')

    deletar_frase(string_digitada)

    treinar_bot_individual(string_digitada, string_corrigida)

    return render_template('index.html', string_digitada=string_digitada, string_resposta=string_corrigida)

if __name__ == '__main__':
    app.run(debug=True)
