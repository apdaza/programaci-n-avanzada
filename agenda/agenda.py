from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'helloworld'
app.config['MYSQL_DATABASE_DB'] = 'agenda'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 6603
mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()

@app.route('/usuarios')
def ver_usuarios():
    cursor.execute("SELECT * from usuarios")
    data = cursor.fetchall()
    return render_template('usuarios.html', usuarios = data )

@app.route('/contactos')
def ver_contactos():
    cursor.execute("SELECT usu_nombre, con_nombre, con_apellido, con_direccion, con_telefono, con_email " +
                    "FROM usuarios as usu " + 
                    "INNER JOIN contactos as con on (usu.usu_id = con.usu_id) ")
    data = cursor.fetchall()
    return render_template('contactos.html', contactos = data )

@app.route('/citas')
def ver_citas():
    cursor.execute("SELECT usu_nombre, con_nombre, con_apellido, con_telefono, cit_lugar, cit_fecha, cit_hora, cit_descripcion " +
                    "FROM usuarios as usu " + 
                    "LEFT JOIN contactos as con on (usu.usu_id = con.usu_id) " +
                    "LEFT JOIN citas as cit on (con.con_id = cit.con_id)")
    data = cursor.fetchall()
    return render_template('citas.html', citas = data )

@app.route('/todos')
def ver_todos():
    cursor.execute("SELECT usu_nombre, con_nombre, con_apellido, con_telefono, cit_lugar, cit_fecha " +
                    "FROM usuarios as usu " + 
                    "LEFT JOIN contactos as con on (usu.usu_id = con.usu_id) " +
                    "LEFT JOIN citas as cit on (con.con_id = cit.con_id)")
    data = cursor.fetchall()
    return render_template('todos.html', citas = data )

@app.route("/agregar_usuario", methods = ['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombre = request.form["nombre"]
        clave = request.form["clave"]
        cursor.execute("""INSERT INTO `usuarios`(`usu_nombre`, `usu_clave`) VALUES (%s, sha1(%s));""", (nombre, clave)) 
        conn.commit()
        return redirect(url_for('ver_usuarios'))
    else:
        return render_template('agregar_usuario.html')

@app.route('/actualizar_usuario', methods=['GET', 'POST'])
def actualizar_usuario():
    if request.method == 'POST':
        id = request.form["id"]
        nombre = request.form["nombre"]
        clave = request.form["clave"]
        cursor.execute("""UPDATE `usuarios` SET `usu_nombre`=%s,`usu_clave`=sha1(%s) WHERE `usu_id`= %s""", (nombre, clave, id)) 
        conn.commit()
        return redirect(url_for('ver_usuarios'))
    else:
        id = request.args["id"]
        cursor.execute("SELECT usu_id, usu_nombre from usuarios where usu_id = " + id)
        usuario = cursor.fetchone()
        return render_template('editar_usuario.html', usuario=usuario)
        

@app.route('/eliminar_usuario', methods=['GET'])
def eliminar_usuario():
    if request.method == 'GET':
        id = request.args["id"]
        cursor.execute("DELETE from usuarios where usu_id = " + id)
        conn.commit()
        return redirect(url_for('ver_usuarios'))


if __name__ == '__main__':
    app.run(debug=True)
