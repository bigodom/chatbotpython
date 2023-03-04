
import sqlite3
from difflib import SequenceMatcher

# conectando ao banco de dados
conexao = sqlite3.connect('banco.db')

# cursor para executar comandos sql
cursor = conexao.cursor()

# criando tabela para armazenar dados
cursor.execute("CREATE TABLE IF NOT EXISTS chatbot (frase text, resposta text)")
conexao.close()

def responder_bot(frase):
    # buscando frase e resposta no banco de dados
    conexao = sqlite3.connect('banco.db')
    print('Conectado ao banco de dados')
    cursor = conexao.cursor()
    cursor.execute("SELECT resposta FROM chatbot WHERE frase LIKE ?", (frase,))
    resultado = cursor.fetchone()
    

    if resultado is not None:
        return resultado[0]

    # caso a frase não exista no banco de dados
    if resultado is None:
        # busca a frase mais parecida
        cursor.execute("SELECT frase, resposta FROM chatbot")
        resultado = cursor.fetchall()
        maior_similaridade = 0
        resposta_mais_parecida = ''

        for r in resultado:
            similaridade = SequenceMatcher(None, frase, r[0]).ratio()
            if similaridade > maior_similaridade:
                maior_similaridade = similaridade
                resposta_mais_parecida = r[1]
        
        # salva a frase e a resposta do usuário
        cursor.execute("INSERT INTO chatbot VALUES (?, ?)", (frase, resposta_mais_parecida))
        conexao.commit()
        conexao.close()

        return resposta_mais_parecida
    else:
        return resultado[0]


# loop para continuar o chat
#while True:
#    frase = input('Digite uma frase: ')
#    resposta = responder_bot(frase)
#    print('Bot:', resposta)