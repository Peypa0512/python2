from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# conexión SQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'usuarios'

conexion = MySQL(app)

# la ruta raiz

@app.route('/')
def index():
    # esto es una vista que se expresa en una función para ver que funciona la página y va a estar ligada a la ruta
    # raiz con el decorador de arriba
    #return "¡Hola Mundo!"

    # para que sea una hoja dinamica...
    # también pueden pasarse lista...

    cursos = ['PHP', 'Python', 'Java', 'Kotlin', 'Dart', 'JavaScript']
    data = {'titulo': 'Index1234', 'bienvenida': 'Saludos', 'cursos': cursos, 'num_cursos': len(cursos) }
    return render_template('index.html',data=data)

# decorador antes de la petición para realizar acciones antes
@app.before_request
def before_request():
    print('Antes de la petición...')


# decorador después de la petición que hace el usuario
@app.after_request
def after_request(respuesta):
    print('después de la petición')
    return respuesta


# vamos a crear una url personalizada, imaginate una url con el nombre de cada usuario
@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
            'titulo': 'Contacto',
            'nombre': nombre,
            'edad': edad
    }

    return render_template('contacto.html', data = data)



# query string

def query_string():
    print(request)      #la solicitud que hace el usuario
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return 'ok'


#vista de la querys de db
@app.route('/usuario')
def listar_usuario():
    data = {}
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM `usuarios` WHERE `COL 5` like '%live%';"
        cursor.execute(sql)
        usuarios = cursor.fetchall()
        #print(usuarios)
        data['usuarios'] = usuarios
        data['mensaje'] = 'Exito'
    except Exception as ex:
        data['mensaje']= 'ERROR....'
    return jsonify(data)  #la respuesta se guardará en un json



# para controlar el error del código 404

def pagina_no_encontrada(error):
    # return render_template('404.html'),404
    return redirect(url_for('index'))


if __name__ == '__main__':
    #para no estar todo el rato parando y volviendo a arrancar el servidor podremos dentro de run

    # url en la que se accede la query_string
    app.add_url_rule('/query_string', view_func= query_string)  # view_func es funcion que va a estar asociada a url
    # vamos a hacer el regulador de la funcion de errores
    app.register_error_handler(404, pagina_no_encontrada)
    # para cambiar el puerto dentro de run() con port= puedo poner el puerto que quieras.
    app.run(debug=True,)


# vamos a conectarnos a una base de datos, phpadmin, lo primero pip install flask-mysqldb, comprobar una vez instalado
# mysqlclient y flask-mysql que son las 2 librerias que vamos a utilizar para este caso.