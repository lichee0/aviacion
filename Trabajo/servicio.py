from gc import collect
from tokenize import Double
from flask import Flask, Response, jsonify
from datos import *
from demoFirestore import *



#instancia de la clase Flask
Miservidor = Flask(__name__)
#rutas http para acceder desde un navegador web
@Miservidor.route('/')
def inicio():
    return '<B> Mi primera aplicacion Web </B> con Python y Flask'

@Miservidor.route('/chiste')
def chiste():
   return '<B> Cuando un programa nace, no llora.. </B>/br dice Hola mundo!!'

@Miservidor.route('/pagina_1')
def funcion_simple():
    return '<H1> Página 1 </H1> Ejemplo de ruta simple.'

@Miservidor.route("/saludo/<nombre>,<deseo>")
def saludo(nombre, deseo):
    return f"<H1> <center>  Hola {nombre}, Bienvenido.\
    <br> Cumpliremos tu deseo: {deseo} "

@Miservidor.route('/dollar2cop/<cop>')
def convertirDollar2cop(cop):
    valor = 3.783
    try:
        valor = float (cop) / valor
        return f'<H1>Para ${cop} Pesos Colombianos, obtines US${valor}'
    except:
        return '<H1> <center> Escriba bien los numeros cabezon...'

from datos import *
@Miservidor.route('/insertar<nombre>,<edad>')
def insertarBD(nombre,edad):
    conexion = conectar ('solodatos.db')
    comandoSQL = f'''
        INSERT INTO CLIENTE (nombre, edad)
        VALUES ('{nombre}', {edad});
    '''
    InsertarDatos(conexion,comandoSQL)
    return "Datos Almacenados Exitosamente "


@Miservidor.route('/listar_Personas')
def listarPersonas():
    conexion = conectar ('solodatos.db')
    comandoSQL = f'''
        SELECT * FROM CLIENTE
    '''
    data = ConsultarTodos(conexion, comandoSQL)
    texto = 'DATOS <br>'
    for item in data:
        texto = texto + str(item) + "<br>"
    return texto

#FireBase

@Miservidor.route('/f_seleccionar/')
def servicio_seleccionar():
    try:
        data = f_seleccionarTodos("registro exclusivo")
        data1 = f_seleccionarTodos("registro aviacion")
        data2 = f_seleccionarTodos("registro exclusivo2")
        print(data)
        print(data1)
        print(data2)
        #return(data)
        #return response(data, status=200, mimetype='application/json')
        return jsonify({'message': "Consultada realizada",
                        'object': "list",
                        'data' : data,
                        'data1':data1,
                        'data2':data2,
                       }
                       ),200
    except:
        return Response("{'a':'b'}", status=300, mimetype='application/json')

@Miservidor.route('/f_insertarc/<nombre>,<edad>')
def servicio_insertarc(nombre,edad):
    try:
        data = {}
        data['nombre']= nombre
        data['edad']= edad
        documento = nombre
        coleccion = "registro exclusivo"
        f_adicionar(coleccion,documento,data)
        return jsonify({'message': "Consultada realizada",
                        'object': "list",
                        'data' : data,
                       }
                       ),200
    except:
        return jsonify({'message': "Error de usuario",
                        'object': "list",
                        'data' : data,
                       }
                       ),300

@Miservidor.route('/f_insertara/<nombre>')
def servicio_insertara(nombre):
    try:
        data = {}
        data['nombre']= nombre
        documento = nombre
        coleccion = "registro aviacion"
        f_adicionar(coleccion,documento,data)
        return jsonify({'message': "Consultada realizada",
                        'object': "list",
                        'data' : data,
                       }
                       ),200
    except:
        return jsonify({'message': "Error de usuario",
                        'object': "list",
                        'data' : data,
                       }
                       ),300

@Miservidor.route('/f_insertare/<nombre>,<edad>,<cargo>')
def servicio_insertare(nombre,edad,cargo):
    try:
        data = {}
        data['nombre']= nombre
        data['edad']= edad
        data['cargo']=cargo
        documento = nombre
        coleccion = "registro exclusivo2"
        f_adicionar(coleccion,documento,data)
        return jsonify({'message': "Consultada realizada",
                        'object': "list",
                        'data' : data,
                       }
                       ),200
    except:
        return jsonify({'message': "Error de usuario",
                        'object': "list",
                        'data' : data,
                       }
                       ),300

@Miservidor.route('/f_actualizar/<documento>,<edad>')
def servicio_actualizar(documento,edad):
    data = {}
    data['edad']= edad
    data['nombre']=nombre
    documento = documento
    coleccion = "registro aviacion"
    coleccion = "registro exclusivo"
    f_modificar(coleccion,documento,data)



@Miservidor.route('/f_borrar/<nombre>')
def servicio_borrar(nombre):
    documento = nombre
    coleccion = "registro exclusivo"
    coleccion = "registro aviacion"
    f_eliminar(coleccion,documento)


#función principal, activa el servidor como aplicación web
# y un seguimiento de mensajes con el debug en True
if __name__ == '__main__':
    Miservidor.run(debug=True)