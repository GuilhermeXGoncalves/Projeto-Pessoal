import sqlite3

conexao = sqlite3.connect('web.db' , check_same_thread=False)
cursor = conexao.cursor()

#Criando Tabela de Usuários
def criarTabelaDeUsuarios():
    comando = 'CREATE TABLE IF NOT EXISTS usuarios (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, senha VARCHAR(10) NOT NULL, email VARCHAR(48) NOT NULL)'
    cursor.execute(comando)
    conexao.commit()