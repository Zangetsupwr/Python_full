from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.users import Users


# RUTA PARA VER TODOS LOS USUARIOS
@app.route('/users')
def view_user():
    user_list = Users.all()
    return render_template('users/view.html', users=user_list)

# RUTA DEL FORMULARIO DE CREACIÓN DE USUARIOS


@app.route('/users/create', methods=['GET'])
def create_user():
    return render_template('users/create.html')

# RUTA PARA CREAR UN USUARIO QUE RECIBE LOS DATOS DEL FORMULARIO


@app.route('/users/create', methods=['POST'])
def create_user_post():
    # request.form es un diccionario que contiene los datos del formulario

    new_user = Users(request.form)
    Users.save(new_user.__dict__())
    return redirect('/users')

# RUTA PARA VER LOS DETALLES DE UN USUARIO


@app.route('/users/<int:id>')
def detail_user(id):
    # Buscamos al usuario por su id
    user = Users.find_by_id(id)
    user.get_referred_users().get_referrer()
    return render_template('users/detail.html', usuario=user)

# RUTA PARA EDITAR UN USUARIO

@app.route('/users/<int:id>/edit')
def edit_user(id):
    # Buscamos al usuario por su id
    user = Users.find_by_id(id)
    return render_template('users/edit.html', usuario=user)

# RUTA PARA ACTUALIZAR LOS DATOS DE UN USUARIO


@app.route('/users/<int:id>/edit', methods=['POST'])
def edit_user_post(id):
    # Creamos un objeto de la clase Users con los datos del formulario
    updated_user = Users(request.form)
    # Asignamos el id al objeto
    updated_user.id = id
    # Actualizamos los datos del usuario
    Users.update(updated_user.__dict__())
    return redirect('/users')

# RUTA PARA ELIMINAR UN USUARIO


@app.route('/users/<int:id>/delete')
def delete_user(id):
    Users.delete_by_id(id)
    return redirect('/users')
