from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'clave_super_secreta'

# Diccionario de usuarios registrados
USUARIOS_REGISTRADOS = {
    'Admin@correo.com': {
        'nombre': 'Admin',
        'apellido': 'Perez',
        'usuario': 'Admin',
        'password': '123'
    }
}

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario_input = request.form['usuario']
        password = request.form['password']

        # Buscar por email o usuario
        usuario_encontrado = None
        email_encontrado = None
        
        for email, datos in USUARIOS_REGISTRADOS.items():
            if email == usuario_input or datos.get('usuario') == usuario_input:
                if datos['password'] == password:
                    usuario_encontrado = datos.get('usuario', datos['nombre'])
                    email_encontrado = email
                    break

        if usuario_encontrado:
            # Guardar datos en la sesión
            session['usuario'] = usuario_encontrado
            session['email'] = email_encontrado
            flash(f'¡Bienvenido de nuevo, {usuario_encontrado}!', 'success')
            return redirect(url_for('inicio'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        usuario = request.form['usuario']
        password = request.form['password']
        password2 = request.form['password2']

        # Validaciones
        if email in USUARIOS_REGISTRADOS:
            flash('Este correo ya está registrado', 'warning')
            return redirect(url_for('registro'))

        if password != password2:
            flash('Las contraseñas no coinciden', 'danger')
            return redirect(url_for('registro'))

        if len(password) < 3:
            flash('La contraseña debe tener al menos 3 caracteres', 'warning')
            return redirect(url_for('registro'))

        # Registrar nuevo usuario
        USUARIOS_REGISTRADOS[email] = {
            'nombre': nombre,
            'apellido': apellido,
            'usuario': usuario,
            'password': password
        }

        # Iniciar sesión automáticamente
        session['usuario'] = usuario
        session['email'] = email
        flash(f'¡Registro exitoso! Bienvenido, {usuario}!', 'success')
        return redirect(url_for('inicio'))

    return render_template('registro.html')

@app.route('/logout')
def logout():
    usuario = session.get('usuario', 'Usuario')
    session.pop('usuario', None)
    session.pop('email', None)
    flash(f'Hasta pronto, {usuario}. Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('inicio'))

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

@app.route('/papacalavera')
def papacalavera():
    return render_template('papacalavera.html')

if __name__ == '__main__':
    app.run(debug=True)