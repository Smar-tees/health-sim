import sqlite3

def retrieve():
    # Connect to the SQLite database
    connection = sqlite3.connect('db')

    # Create a cursor object
    cursor = connection.cursor()

    # Query to retrieve data
    cursor.execute('SELECT * FROM patients')

    # Fetch all rows from the last executed query
    patients = cursor.fetchall()

    # Iterate through the rows and print them
    for patient in patients:
        print(patient)

    # Close the connection
    connection.close()

retrieve()