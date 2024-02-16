import sqlite3

conexao = sqlite3.connect('web.db' , check_same_thread=False)
cursor = conexao.cursor()

