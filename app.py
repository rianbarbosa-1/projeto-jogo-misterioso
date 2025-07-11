from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'chave-secreta'  # Necessário para usar sessões

@app.route('/jogar', methods=['GET', 'POST'])
def jogar():
    if 'numero' not in session:
        session['numero'] = random.randint(1, 10)
        session['tentativas'] = 3

    mensagem = ''
    if request.method == 'POST':
        palpite = int(request.form['palpite'])
        numero_correto = session['numero']
        session['tentativas'] -= 1

        if palpite == numero_correto:
            mensagem = f'🎉 Parabéns! Você acertou o número {numero_correto}.'
            session.pop('numero')
            session.pop('tentativas')
        elif session['tentativas'] <= 0:
            mensagem = f'💥 Você perdeu! O número era {numero_correto}.'
            session.pop('numero')
            session.pop('tentativas')
        else:
            if palpite < numero_correto:
                mensagem = '📉 Muito baixo! Tente novamente.'
            else:
                mensagem = '📈 Muito alto! Tente novamente.'

    tentativas = session.get('tentativas', 3)
    return render_template('jogar.html', tentativas=tentativas, mensagem=mensagem)

@app.route('/')
def inicio():
    return redirect(url_for('jogar'))

if __name__ == '__main__':
    app.run(debug=True)
