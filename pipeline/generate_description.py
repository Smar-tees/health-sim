import random
from Creation.connection import create_run

prompt = '''Please give me a list five to seven possible symptoms that someone with {} would have 
            in the format of a python list please. In the text block please litterally give me nothing
            except for a python list like: [Stuffy nose, cough, chills].'''
assistant_id='asst_N8y3Cosh8Zw9ec5F4M5BNKqg'


def generate_description():
    r = random_illness()
    p = prompt.format(r)
    message = create_run(assistant_id, p)
    return message, r


def random_illness():
    return random.choice(['Tuberculosis', 'Influenza'])