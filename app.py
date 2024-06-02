from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    usuarios = conn.execute('SELECT * FROM usuarios').fetchall()
    conn.close()
    return render_template('index.html', usuarios=usuarios)

@app.route('/feminino')
def feminino():
    return render_template('feminino.html')

@app.route('/masculino')
def masculino():
    return render_template('masculino.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Aqui você pode inserir os dados no banco de dados ou fazer qualquer validação necessária
        conn = get_db_connection()
        conn.execute('INSERT INTO usuarios (nome_usuario, senha) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()

        # Redirecionar para a página inicial após o login
        return redirect(url_for('index'))
    
    # Se o método for GET, renderizar o formulário de login
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
