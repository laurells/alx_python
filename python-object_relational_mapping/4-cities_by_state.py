import MySQLdb
import sys

# Check for the correct number of command-line arguments
if len(sys.argv) != 4:
    print("Usage: python3 4-cities_by_states.py <username> <password> <database>")
    sys.exit(1)

# Extract command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

try:
    # Connect to the MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Prepare the SQL query to fetch all cities
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id"

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows
    cities = cursor.fetchall()

    # Display the results as they are in the example
    for city in cities:
        print(city)

    # Close the cursor and connection
    cursor.close()
    conn.close()

except MySQLdb.Error as e:
    print("MySQL Error:", e)
    sys.exit(1)