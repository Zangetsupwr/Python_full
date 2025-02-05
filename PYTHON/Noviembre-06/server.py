
# Importar Flask
from flask import Flask, redirect, render_template, request

# Crear una instancia de Flask
app = Flask(__name__)


# RUTAS

# Definir una ruta para el recurso raíz del sitio
@app.route('/')
def index():
    return redirect('/registro')


@app.route('/registro')
def root():
    return render_template('index.html')


@app.route('/registro', methods=['POST'])
def registro():
    formulario = request.form
    # usamos la clave [] para obtener el valor de un campo del formulario
    print(formulario.get('nombreIpt'))
    print(formulario['pwdIpt'])
    print(formulario.get('nameIpt'))
    # usamos el método getlist para obtener los valores de un campo que es una lista en el formulario
    print(formulario.getlist('marcaIpt'))

    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



# Iniciar la aplicación
if __name__ == '__main__':
    # Iniciar la aplicación en modo debug para recargar automáticamente los cambios en el código
    app.run(debug=True)
