@app.route('/update_property_details', methods=['PUT'])
def update_property_details():
    property_id = request.json['property_id']
    property_name = request.json['property_name']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']

    cur = mysql.connection.cursor()

    # Update the property in the database
    cur.execute("UPDATE properties SET property_name = %s, address = %s, city = %s, state = %s WHERE property_id = %s", (property_name, address, city, state, property_id))
    mysql.connection.commit()

    # Retrieve all properties from the database
    cur.execute("SELECT * FROM properties")
    properties = cur.fetchall()

    return jsonify({'properties': properties})
