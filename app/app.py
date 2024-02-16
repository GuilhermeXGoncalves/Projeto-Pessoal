from flask import Flask, render_template, redirect, request, flash
from control import usuario


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
    
    if nome == 'guilherme' and senha == '123':
        return render_template('usuario.html')
    else:
        flash('Usuário Inválido')
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


@app.route('/usuarios' , methods=['GET'])
def lerUsuarios():
    return usuario.lerUsuario()


if __name__ in "__main__":
    app.run(debug=True)
