import database
conexao = database.conexao
cursor = database.conexao.cursor()

def lerUsuario():
    comando = f'SELECT id, nome, senha, email FROM usuarios'
    cursor.execute(comando)
    usuarios = cursor.fetchall()
    return usuarios