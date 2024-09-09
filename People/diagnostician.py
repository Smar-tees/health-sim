'''
This is going to be the model that is in charge of looking through data to determine what illness 
the patient has. The diagnostician will also determine which medical tests are requested for the 
intern to find results for, if it is an imaging test like a CT scan, MRI, or X-ray then the 
radiologist will find the results instead. 
'''

import sqlite3
from pipeline.generate_tests import generate_tests
from People.receptionist import updatePatient


def orderTests(id):

    message = generate_tests(id)
    tests = message.data[0].content[0].text.value
    tests = tests[tests.find('['):tests.find(']')+1]

    updatePatient(id, 'testsOrdered', str(tests))



