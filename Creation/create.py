# Structure Of the Database:
# The structure will look like cases - With different tables for each patient's case
# There will be a name of the patient, what their description of symptoms was, the medical tests 
# that were ordered and their results, what the condition was and what the machine thought

# As a part of both condition and prediction make sure to add a severity to both of the values, mild, medium, and severe

import sqlite3

connection = sqlite3.connect('db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
               id INTEGER PRIMARY KEY, 
               name TEXT, 
               age INTEGER, 
               description TEXT, 
               testsOrdered TEXT, 
               testResults TEXT, 
               prediction TEXT, 
               condition TEXT
               );''')
cursor.executemany('INSERT INTO patients (name, age) VALUES (?, ?)', [
    ("Test", 7), ("other test", 18), ("one more test", 98)])

# in order to update rows with more information use UPDATE into
# IT IS REQUIRED TO GET id SO THAT YOU CAN EDIT THAT SPECIFIC ROW
# id = cursor.lastrowid must use execute rather than executemany

connection.commit()

connection.close()