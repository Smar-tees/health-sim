'''
This is the model that will determine what the results are of each medical test, except for ones 
that require imaging. Imaging results will be analyzed by the radiologist. 
'''

from pipeline.generate_results import generate_results
from People.receptionist import updatePatient

def testResults(id):

    message = generate_results(id)
    results = message.data[0].content[0].text.value
    results = results[results.find('{'):results.rfind('}')+1]

    updatePatient(id, 'testResults', str(results))