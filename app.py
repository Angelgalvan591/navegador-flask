from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'sonic_secret_key_2025'

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    password = request.form['password']
    
    # Validación simple
    if usuario == "sonic" and password == "123":
        return render_template('bienvenido.html', usuario=usuario)
    else:
        return render_template('login.html', error=True)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        usuario = request.form['usuario']
        password = request.form['password']
        password2 = request.form['password2']
        
        if password != password2:
            flash('Las contraseñas no coinciden')
            return redirect('/registro')
        
        # Registro exitoso - mostrar bienvenida
        return render_template('bienvenido.html', usuario=usuario)
    
    return render_template('registro.html')

@app.route('/animales')
def animales():
    return render_template('animales.html')

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

if __name__ == '__main__':
    app.run(debug=True)