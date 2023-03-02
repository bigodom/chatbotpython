import sqlite3

# conectando ao banco de dados
conexao = sqlite3.connect('banco.db')

# cursor para executar comandos sql
cursor = conexao.cursor()

def treinar_bot_individual():
     frase = input('Digite uma frase: ')
     resposta = input('Digite a resposta: ')
     cursor.execute("INSERT INTO chatbot VALUES (?, ?)", (frase, resposta))
     conexao.commit()

def treinar_bot():
    frase = [
        'oi',
        'ola',
        'bom dia',
        'boa tarde',
        'boa noite',
        'opções',
        'cardapio',
        'gostaria de uma pizza 4 queijos',
        'gostaria de uma pizza muzzarella',
        'gostaria de uma pizza frango com catupiri',
        'gostaria de uma pizza calabresa',
        'gostaria de uma pizza portuguesa',
        'gostaria de uma pizza a moda',
        'gostaria de uma pizza',
        'cartão',
        'pix',
        'dinheiro',
        'obrigado',
        'eu que agradeço'
    ]
    resposta = [
        'olá, gostaria de fazer um pedido?',
        'olá, gostaria de fazer um pedido?',
        'bom dia, gostaria de fazer um pedido?',
        'boa tarde, gostaria de fazer um pedido?',
        'boa noite, gostaria de fazer um pedido?',
        'fazer um pedido, ver o cardápio, conversar com o atendente',
        'temos as seguintes opções: pizza ( 4 queijos, muzzarella, frango com catupiri, calabresa, portuguesa e a moda)',
        'pizza 4 queijos, o valor é R$ 30,00 gostaria de pagar com cartão, pix ou dinheiro?',
        'pizza muzzarella, o valor é R$ 30,00 gostaria de pagar com cartão, pix ou dinheiro?',
        'pizza frango com catupiri, o valor é R$ 30,00 gostaria de pagar com cartão, pix ou dinheiro?',
        'pizza calabresa, o valor é R$ 30,00 gostaria de pagar com cartão, pix ou dinheiro?',
        'pizza portuguesa, o valor é R$ 30,00 gostaria de pagar com cartão, pix ou dinheiro?',
        'pizza a moda, o valor é R$ 30,00 gostaria de pagar com cartão, pix ou dinheiro?',
        'qual pizza gostaria?',
        'ok, seu pedido foi realizado! Obrigado pela preferência!',
        'ok, seu pedido foi realizado! Obrigado pela preferência!',
        'ok, seu pedido foi realizado! Obrigado pela preferência!',
        'nós agradecemos a preferência!',
        'não tem de quê!'
    ]
    
    for i in range(len(frase)):
        cursor.execute("INSERT INTO chatbot VALUES (?, ?)", (frase[i], resposta[i]))
        conexao.commit()

def limpar_banco():
    cursor.execute("DELETE FROM chatbot")
    conexao.commit()

# Caso queira treinar o bot individualmente descomente a linha abaixo
#while True:
#    treinar_bot_individual()

# Caso queira limpar o banco de dados descomente a linha abaixo
#limpar_banco()

treinar_bot()

conexao.close()