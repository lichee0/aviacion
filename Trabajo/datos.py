import sqlite3 

def conectar(nombre_basedatos):
    conDB = sqlite3.connect(nombre_basedatos)
    return conDB

def crearTabla(conexion, comandoSQL):
    cur = conexion.cursor()
    cur.execute(comandoSQL)

def InsertarDatos(conexion, comandoSQL):
    cur = conexion.cursor()
    cur.execute(comandoSQL)
    conexion.commit()

def ConsultarTodos(conexion, comandoSQL):
     cur = conexion.cursor()
     cur.execute(comandoSQL)
     datos = cur.fetchall()
     print (type(datos))
     return datos

def Actualizar (conexion, comandoSQL):
    cur = conexion.cursor()
    cur.execute(comandoSQL)
    conexion.commit()

def Eliminar(conexion, comandoSQL):
    cur = conexion.cursor()
    cur.execute(comandoSQL)
    conexion.commit()


if __name__ == '__main__':
    conexion = conectar('soloDatos.db')
    comandoSQL = '''
        CREATE TABLE IF NOT EXISTS CLIENTE(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER
         )
    '''
    #crearTabla(conexion,comandoSQL)

    #id = int(input("ID?"))
    nombre = input("Nombre?")
    edad = int(input("Edad?"))

    #comandoSQL = f'''
    #    INSERT INTO CLIENTE (nombre, edad)
    #    VALUES ('{nombre}', {edad});
    #'''
    #InsertarDatos(conexion,comandoSQL)

    #comandoSQL = '''
    #    SELECT * FROM CLIENTE
    #'''
    #data = ConsultarTodos(conexion, comandoSQL)
    #for item in data:
    #    print(item)

    

    comandoSQL = '''
        UPDATE CLIENTE 
        SET nombre = 'Juan' 
        WHERE id = 1
    '''
    Actualizar(conexion,comandoSQL)

    
    comandoSQL = '''
       DELETE from CLIENTE where id = 1
    '''
    Eliminar(conexion,comandoSQL)
