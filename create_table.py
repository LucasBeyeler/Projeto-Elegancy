import sqlite3

def create_table():
    # Conecta ao banco de dados (cria o arquivo se ele não existir)
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Cria a tabela 'usuarios'
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_usuario TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

    # Confirma a transação
    conn.commit()
    # Fecha a conexão com o banco de dados
    conn.close()

if __name__ == '__main__':
    create_table()