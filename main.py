from pipeline.generate_description import generate_description
from pipeline.generate_tests import generate_tests
from pipeline.generate_results import generate_results
import sqlite3
import time
from People.receptionist import new_patient
from Creation.retrieve import retrieve
from People.diagnostician import orderTests
from People.intern import testResults




id = new_patient()
orderTests(id)
testResults(id)
retrieve()






































'''
message, illness = generate_description()
symptoms = eval(message.data[0].content[0].text.value)['symptoms']

connection = sqlite3.connect('db')
cursor = connection.cursor()

cursor.execute('INSERT INTO patients (description, condition) VALUES (?, ?)', [str(symptoms), illness])
connection.commit()
id = cursor.lastrowid

time.sleep(5)
message = generate_tests(id)
tests = message.data[0].content[0].text.value

query = '''
# UPDATE patients
# SET testsOrdered = ?
# WHERE id = ?
'''
cursor.execute(query, (tests, id))
connection.commit()

print(id)
time.sleep(5)
message = generate_results(id)
results = message.data[0].content[0].text.value

query = '''
# UPDATE patients
# SET testResults = ?
# WHERE id = ?
'''
cursor.execute(query, (results, id))


connection.commit()
connection.close()
'''