import sqlite3
conexao = sqlite3.connect('web.db' , check_same_thread=False)
cursor = conexao.cursor()

#Criando Tabela de Usuários
def criarTabelaDeUsuarios():
    comando = 'CREATE TABLE IF NOT EXISTS usuarios (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, senha VARCHAR(10) NOT NULL, email VARCHAR(48) NOT NULL)'
    cursor.execute(comando)
    conexao.commit()


def criarUser(nome, senha, email):
    comando = f'INSERT INTO usuarios (nome,senha,email) VALUES ("{nome}" , "{senha}" , "{email}")'
    cursor.execute(comando)
    conexao.commit()

def adicionaAtt():
    criarUser('Herbert' , 'Hp1234' , 'herbert121@gmail.com')
    criarUser('Guilherme' , 'Gg1234' , 'guilherme121@gmail.com')
    criarUser('Lara' , 'Ll1234' , 'lara121@gmail.com')


criarTabelaDeUsuarios()
adicionaAtt()