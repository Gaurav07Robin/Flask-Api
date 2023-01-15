@app.route('/fetch_property_details', methods=['GET'])
def fetch_property_details():
    city = request.args.get('city')

    cur = mysql.connection.cursor()

    # Retrieve all properties from the database that belong to the specified city
    cur.execute("SELECT * FROM properties WHERE city = %s", (city,))
    properties = cur.fetchall()

    return jsonify({'properties': properties})
