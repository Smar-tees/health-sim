import sqlite3
from Creation.connection import create_run

prompt = '''Given this list of symptoms: {}. Give me a list of three medical tests from this list: {}, 
            that would help narrow down causes. Please give them in the format of a python list. DO
            NOT PICK CHEST X-RAY. '''
assistant_id='asst_jidazm1S950hcqXQoyR5B3uE'

medical_tests = [
    "24-Hour Urine Collection",
    "Allergy Testing",
    "Basic Metabolic Panel (BMP)",
    "B-Type Natriuretic Peptide (BNP) Test",
    "C-Reactive Protein (CRP)",
    "Complete Blood Count (CBC)",
    "Comprehensive Metabolic Panel (CMP)",
    "Electrocardiogram (EKG)",
    "Fecal Immunochemical Test (FIT)",
    "Fecal Occult Blood Test (FOBT)",
    "Hemoglobin A1c",
    "Lipid Panel",
    "Liver Function Tests (LFTs)",
    "Microalbumin Test",
    "Pap Smear (Pap Test)",
    "Prothrombin Time (PT) and International Normalized Ratio (INR)",
    "Pulmonary Function Tests (PFTs)",
    "Stool Culture",
    "Thyroid Function Tests",
    "Urinalysis",
    "Urine Culture"
]

def generate_tests(row_id):
    r = find_symptoms(row_id)
    p = prompt.format(r, str(medical_tests))
    message = create_run(assistant_id, p)
    return message

def find_symptoms(row_id):
    connection = sqlite3.connect('db')
    cursor = connection.cursor()
    cursor.execute("SELECT description FROM patients WHERE id = ?", (row_id,))
    result = cursor.fetchone()
    connection.commit()
    connection.close()
    return result