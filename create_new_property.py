from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'your_database'
app.config['MYSQL_HOST'] = 'your_host'

mysql = MySQL(app)

@app.route('/create_new_property', methods=['POST'])
def create_new_property():
    property_name = request.json['property_name']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']

    cur = mysql.connection.cursor()

    # Insert the property into the database
    cur.execute("INSERT INTO properties (property_name, address, city, state) VALUES (%s, %s, %s, %s)", (property_name, address, city, state))
    mysql.connection.commit()

    # Retrieve all properties from the database
    cur.execute("SELECT * FROM properties")
    properties = cur.fetchall()

    return jsonify({'properties': properties})
