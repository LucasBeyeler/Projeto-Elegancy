import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Criação de uma tabela exemplo
c.execute('''CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT, email TEXT)''')

conn.commit()
conn.close()
