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

@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome, email))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
