import random
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave-secreta'  # Defina uma chave secreta para usar sessões

ranking = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        if not nome:
            return render_template('index.html', erro="Por favor, insira seu nome.")

        # Iniciar o jogo
        session['nome'] = nome
        session['numero_misterioso'] = random.randint(1, 100)
        session['tentativas_restantes'] = 3
        return redirect(url_for('jogar'))

    return render_template('index.html')

@app.route('/jogar', methods=['GET', 'POST'])
def jogar():
    if 'nome' not in session:
        return redirect(url_for('index'))  # Se não iniciou o jogo

    nome = session['nome']
    numero_misterioso = session['numero_misterioso']
    tentativas_restantes = session['tentativas_restantes']
    mensagem = ""

    if request.method == 'POST':
        palpite = request.form.get('palpite', type=int)
        
        if palpite is None:
            mensagem = "Por favor, insira um número válido."
        elif palpite < 1 or palpite > 100:
            mensagem = "O número deve ser entre 1 e 100."
        else:
            tentativas_restantes -= 1
            session['tentativas_restantes'] = tentativas_restantes

            if palpite == numero_misterioso:
                pontos = 4 - tentativas_restantes
                ranking.append({"nome": nome, "pontos": pontos})
                return redirect(url_for('resultado'))
            elif palpite < numero_misterioso:
                mensagem = "O número misterioso é MAIOR."
            else:
                mensagem = "O número misterioso é MENOR."

            if tentativas_restantes == 0:
                pontos = 0
                ranking.append({"nome": nome, "pontos": pontos})
                return redirect(url_for('resultado'))

    return render_template('jogar.html', nome=nome, tentativas_restantes=tentativas_restantes, mensagem=mensagem)

@app.route('/resultado')
def resultado():
    nome = session.get('nome', '')
    pontos = next((j['pontos'] for j in ranking if j['nome'] == nome), 0)
    ranking_sorted = sorted(ranking, key=lambda x: x['pontos'], reverse=True)
    return render_template('resultado.html', nome=nome, pontos=pontos, ranking=ranking_sorted)

@app.route('/ranking')
def ranking_page():
    ranking_sorted = sorted(ranking, key=lambda x: x['pontos'], reverse=True)
    return render_template('ranking.html', ranking=ranking_sorted)

if __name__ == '__main__':
    app.run(debug=True)