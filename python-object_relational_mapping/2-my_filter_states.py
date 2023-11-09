import MySQLdb
import sys

# Check for the correct number of command-line arguments
if len(sys.argv) != 5:
    print("Usage: python3 2-my_filter_states.py <username> <password> <database> <state_name>")
    sys.exit(1)

# Extract command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

try:
    # Connect to the MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Execute the SQL query with user input using format method to prevent SQL injection
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id", (state_name,))

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results in the specified format
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    conn.close()

except MySQLdb.Error as e:
    print("MySQL Error:", e)
    sys.exit(1)