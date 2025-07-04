import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar o ranking
ranking = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jogar', methods=['POST'])
def jogar():
    nome = request.form['nome']
    numero_misterioso = random.randint(1, 100)
    tentativas_restantes = 3
    pontos = 0

    while tentativas_restantes > 0:
        palpite = request.form.get('palpite', type=int)

        if palpite is None:
            return render_template('index.html', erro="Por favor, insira um número válido.")

        if palpite < 1 or palpite > 100:
            return render_template('index.html', erro="O número deve ser entre 1 e 100.")

        if palpite == numero_misterioso:
            pontos = 4 - tentativas_restantes  # A pontuação é baseada nas tentativas restantes
            break
        elif palpite < numero_misterioso:
            return render_template('index.html', mensagem="O número misterioso é MAIOR.", nome=nome, tentativas_restantes=tentativas_restantes)
        else:
            return render_template('index.html', mensagem="O número misterioso é MENOR.", nome=nome, tentativas_restantes=tentativas_restantes)

        tentativas_restantes -= 1

    # Adiciona o nome e a pontuação ao ranking
    ranking.append({"nome": nome, "pontos": pontos})

    # Ordena o ranking
    ranking_sorted = sorted(ranking, key=lambda x: x['pontos'], reverse=True)

    return render_template('resultado.html', nome=nome, pontos=pontos, ranking=ranking_sorted)

@app.route('/ranking')
def ranking_page():
    ranking_sorted = sorted(ranking, key=lambda x: x['pontos'], reverse=True)
    return render_template('ranking.html', ranking=ranking_sorted)

if __name__ == "__main__":
    app.run(debug=True)
