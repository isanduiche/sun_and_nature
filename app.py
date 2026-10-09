from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('inicio.html')
    return render_template('login.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('cadastro.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        gerente = request.form['gerente']
        if username == 'admin' and password == '' and gerente == '':
            flash('Please enter your password')
            return redirect(url_for('cadastro'))
        else:
            return redirect(url_for('login'))

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/equipamentos')
def equipamentos():
    return render_template('equipamentos.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

if __name__ == '__main__':
    app.run(debug=True)