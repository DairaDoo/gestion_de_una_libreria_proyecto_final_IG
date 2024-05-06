import sys
from flask import Flask, jsonify
import mariadb
from config import DATABASE_CONFIG

app = Flask(__name__)

# Conexión a la base de datos
try:
    connection = mariadb.connect(**DATABASE_CONFIG)
    cursor = connection.cursor()
except mariadb.Error as e:
    print(f"Error al conectarse a la base de datos MariaDB: {e}")
    sys.exit(1)

@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

@app.route('/api/allUsers')
def get_users():
    """Esta función retorna todos los usuarios de la base de datos."""
    try:
        cursor.execute("SELECT * FROM Usuarios")
        users = cursor.fetchall()
        return jsonify(users)
    except mariadb.Error as e:
        print(f"Error al ejecutar la consulta SQL: {e}")
        return jsonify({'error': 'Error al ejecutar la consulta SQL'}), 500

if __name__ == '__main__':
    app.run(debug=True)
