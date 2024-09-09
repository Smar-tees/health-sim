import sqlite3

def deleteData():
    connection = sqlite3.connect('db')
    cursor = connection.cursor()

    # SQL command to delete all rows in the 'patients' table
    cursor.execute('DELETE FROM patients')

    # Commit the changes to the database
    connection.commit()

    # Optionally, check how many rows were deleted
    print(f"Deleted {cursor.rowcount} rows.")

    # Close the connection
    connection.close()

def remakeTable():  

    # Connect to SQLite database
    connection = sqlite3.connect('db')
    cursor = connection.cursor()

    # Create a new table with the correct schema
    cursor.execute('''CREATE TABLE IF NOT EXISTS new_patients (
                id INTEGER PRIMARY KEY, 
                name TEXT, 
                age INTEGER, 
                description TEXT, 
                testsOrdered TEXT, 
                testResults TEXT, 
                prediction TEXT, 
                condition TEXT
                );''')

    # Optional: Copy data from the old table to the new table if you need to preserve existing data
    cursor.execute('INSERT INTO new_patients (name, age) SELECT name, age FROM patients')

    # Drop the old table
    cursor.execute('DROP TABLE patients')

    # Rename the new table
    cursor.execute('ALTER TABLE new_patients RENAME TO patients')

    # Commit changes and close connection
    connection.commit()
    connection.close()

deleteData()