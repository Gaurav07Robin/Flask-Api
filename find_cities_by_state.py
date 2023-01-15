@app.route('/find_cities_by_state', methods=['GET'])
def find_cities_by_state():
    state = request.args.get('state')

    cur = mysql.connection.cursor()

    # Retrieve all city names from the database that belong to the specified state
    cur.execute("SELECT DISTINCT city FROM properties WHERE state = %s", (state,))
    cities = cur.fetchall()

    # Extract the city names from the cursor object
    cities = [city[0] for city in cities]

    return jsonify({'cities': cities})
