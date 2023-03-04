from flask import Flask, render_template, request
from main import *

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')



@app.route('/receber_string', methods=['POST'])
def receber_string():
    
    string_digitada = request.form['string_digitada']
     
    string_resposta = responder_bot(string_digitada)
    
    return render_template('index.html', string_digitada=string_digitada, string_resposta=string_resposta)

if __name__ == '__main__':
    app.run(debug=True)

