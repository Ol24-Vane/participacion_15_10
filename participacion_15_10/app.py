from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Clave para la sesión

# Datos de usuarios 
users = {
    'admin1': '123pass',
    'Vane': '28ramirez'
}

@app.route('/')
def home():
    # Redirige al login si no está autenticado
    if 'username' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificación de credenciales
        if username in users and users[username] == password:
            session['username'] = username  # Guardar usuario en la sesión
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('welcome'))
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'danger')

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' not in session:
        flash('Por favor, inicia sesión primero', 'warning')
        return redirect(url_for('login'))

    username = session['username']
    return render_template('welcome.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)  # Eliminar usuario de la sesión
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
