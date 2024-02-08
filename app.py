from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TESTE'


@app.route('/', methods=['GET'])
def home():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    print(nome)
    print(senha)
    return redirect('/')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    email = request.form.get('email')

    print(nome)
    print(senha)
    print(email)

    return render_template('cadastro.html')


if __name__ in "__main__":
    app.run(debug=True)
