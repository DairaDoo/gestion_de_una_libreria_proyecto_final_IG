import sys
from flask import Flask, jsonify
import mariadb
from config import DATABASE_CONFIG

app = Flask(__name__)

# Connecion a la base de datos
try:
    connection = mariadb.connect(**DATABASE_CONFIG)
except mariadb.Error as e:
    print("Error al conectarse a la base de datos MariaDB.")
    sys.exit(1)


cursor = connection.cursor()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/allUsers')
def get_users():
    """Esta funcion retorna todos los usuarios de la base de datos."""
    cursor.execute("SELECT * FROM Prueba_BookVault")
    users = cursor.fetchall()
    return jsonify(users)
    

if __name__ == '__main__':
    app.run(debug=True)
