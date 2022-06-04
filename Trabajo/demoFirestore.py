import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("aviacion.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def f_adicionar(coleccion, documento, data):
    db.collection(coleccion).document(documento).set(data)

def f_modificar(colecion, documento, data):
    db.collection(colecion).document(documento).update(data) 
    #db.collection(colecion).document(documento).set(data)

def f_eliminar(colecion, documento):
    db.collection(colecion).document(documento).delete() 
    #db.collection(colecion).document(documento).set(data)

def f_seleccionarTodos(colecion):
    docs = db.collection(colecion).stream()
    data = {}
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
        data[doc.id]= doc.to_dict()
    return data

def agregarDato():
    data = {
    'Ciudad': input('Ciudad? '),
    'Departamento': input('Departamento? '),
    'Pais': input('Pais? '),
    'idioma': input('Idioma? '),
    'Moneda': input('Moneda? ')
    }

    # Add a new doc in collection 'cities' with ID 'LA'
    db.collection('ciudades').document('MDE').set(data)
    #db.collection('ciudades').add(data)

if __name__ == '__main__':
    agregarDato()