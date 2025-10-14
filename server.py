from flask import Flask, jsonify, request
# Importacion flask para crear la aplicación web
# jsonify para convertir respuestas en formato json
# request para acceder a datos de las peticiones http
import time
# time para funciones con el tiempo

app = Flask(__name__)
# creamos una instancia de flask __name__ indica el modulo actual

# Simulamos una base de datos de usuarios
users_db = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
    3: {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
}
# Define un diccionario llamado users_db qque simula una base de datos con 3 usuarios
# cada uno tiene un ID unico, nombre y correo

@app.route('/api/users/<int:user_id>', methods=['GET'])
# define una ruta para la aplicacion flask
# la ruta acepta peticiones get en la url 
# donde <user_id> es un parametro entero pasado en la url

def get_user(user_id):
    # define una funcion llamada get_user que se ejecute cuando se recibe una peticion get en la ruta anterior
    # recibe el parametri user_id que proviene de la url
    """Endpoint síncrono para obtener información de un usuario"""
    print(f"🔵 Servidor: Recibida petición para usuario {user_id}")
    # imprime en la consola un mensaje indicando que se recibio un peticion para un usuario especifico
    
    # Simulamos un procesamiento que toma tiempo
    time.sleep(2)  # 2 segundos de "procesamiento"
    
    user = users_db.get(user_id)
    # busca el usuario en el diccionario users_db usando el user_id
    # si no encuentra el usuario, devuele none
    if user:
        # verifica si el usuario fue encontrado
        print(f"🟢 Servidor: Enviando respuesta para usuario {user_id}")
        # impreme en consola un mensaje indicando que se enviara la respuesta con los datos del usuario
        return jsonify({"status": "success", "data": user})
        # devuele una respuesta http con formato json que indica exito y contiene los datos del usuario
    else:
        # caso contrario, si no se encontro el usuario
        print(f"🔴 Servidor: Usuario {user_id} no encontrado")
        # imprime en consola un mensaje indicando que el usuario no fue encontrado 
        return jsonify({"status": "error", "message": "User not found"}), 404
        # devuelve una respuesta http con formato json que indica error
        # junto con un mensaje y código de estado 404

@app.route('/api/users', methods=['POST'])
#  define una ruta para peticiones post en /api/users para crear un nuevo usuario
def create_user():
    # define la funcion create_user que se ejecuta cuando se recibe una peticion
    """Endpoint síncrono para crear un usuario"""
    print("🔵 Servidor: Recibida petición para crear usuario")
    # imprime en consola que se recibio una peticion para crear un usuario
    
    data = request.get_json()
    # obtiene los datos json enviados en el cuerpo de la peticion post y los guarda en la variable data
    if not data or 'name' not in data or 'email' not in data:
        # comprueba si no se enviaron datos o si faltan los campos 'name' o email 
        return jsonify({"status": "error", "message": "Missing required fields"}), 400
        # devuelve un error 400 con mensaje indicando campos faltantes
    
    # Simulamos procesamiento
    time.sleep(1) # pausa de 1 segundo
    
    new_id = max(users_db.keys()) + 1
    # calcula un nuevo ID para el usuario sumando 1 al ID más alto actualmente en users_db

    new_user = {
        "id": new_id,
        "name": data['name'],
        "email": data['email']
    }
    # crea un diccionario con la información del nuevo usuario, incluyendo el nuevo ID

    users_db[new_id] = new_user
    # añade el nuevo usuario al diccionario users_db con su ID como clave

    print(f"🟢 Servidor: Usuario {new_id} creado exitosamente")
    # imprime un mensaje indicando que el usuario fue creado exitosamente

    return jsonify({"status": "success", "data": new_user}), 201
    # devuelve una respuesta HTTP con formato JSON que indica exito
    # contiene los datos del nuevo usuario y un código de estado 201

if __name__ == '__main__':
    # verifica si este archivo esta siendo ejecutado directamente y no importado como modulo

    print("🚀 Iniciando servidor síncrono en http://localhost:5000")
    # imprime un mensaje indicando que el servidor esta iniciando

    app.run(debug=True, host='0.0.0.0', port=5000)
    # inicia la aplicación flask
    # debug=True activa el modo depuración (muestra errores en pantalla y reinicia automaticamente)
    # host='0.0.0.0' hace que el servidor escuche en todas las interfaces de red disponibles
    # port=5000 indica el puerto en el que el servidor estará escuchando




























# class Vehiculo (object):
#     __instancia = None

#     def __new__(cls):
#         if Vehiculo.__instancia is None:
#             print("creacion del objeto")
#             Vehiculo.__instancia = object.__new__(cls)





# if __name__ == '__main__':
#     v1 =  Vehiculo()
#     v2 = Vehiculo()

#     print( v1 is v2)
#     print( id(v1), id(v2))