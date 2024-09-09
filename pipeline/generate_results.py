import sqlite3
from Creation.connection import create_run

prompt = '''For each of the tests in this list: {}. Create a result for this test that would
            fit with this illness: {}. Please give me the results in the form of a 
            python dictionary with the key being the test and the value being a seperate dictionary 
            with the results of the tests. In the results please do not state the illness.'''
assistant_id='asst_iv55H4sxq8n0JdMfSwqQh5XJ'


def generate_results(row_id):
    tests, condition = find_tests(row_id)
    p = prompt.format(tests, condition, condition)
    message = create_run(assistant_id, p)
    return message

def find_tests(row_id):
    connection = sqlite3.connect('db')
    cursor = connection.cursor()

    query = """
    SELECT testsOrdered, condition
    FROM patients
    WHERE id = ?;
    """

    cursor.execute(query, (row_id,))
    result = cursor.fetchone()
    tests, condition = result
    connection.commit()
    connection.close()

    return tests, condition