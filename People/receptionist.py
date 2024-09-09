''' 
This file is in charge of taking all information in and saving it - they will record the:
name, age, gender, original symptoms, medical tests ordered, results of said tests, and illness 
that they had, for each patient. 
'''

import sqlite3
import random
from pipeline.generate_description import generate_description

def new_patient():

    first_names = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth",
    "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen",
    "Christopher", "Nancy", "Daniel", "Margaret", "Matthew", "Lisa", "Anthony", "Betty", "Mark", "Dorothy",
    "Donald", "Sandra", "Steven", "Ashley", "Paul", "Kimberly", "Andrew", "Donna", "Joshua", "Emily",
    "Kenneth", "Michelle", "Kevin", "Carol", "Brian", "Amanda", "George", "Melissa", "Edward", "Deborah",
    "Ronald", "Stephanie", "Timothy", "Rebecca", "Jason", "Laura", "Jeffrey", "Helen", "Ryan", "Sharon",
    "Jacob", "Cynthia", "Gary", "Kathleen", "Nicholas", "Amy", "Eric", "Shirley", "Jonathan", "Angela",
    "Stephen", "Anna", "Larry", "Ruth", "Justin", "Brenda", "Scott", "Pamela", "Brandon", "Nicole",
    "Benjamin", "Katherine", "Samuel", "Virginia", "Gregory", "Catherine", "Alexander", "Christine",
    "Frank", "Samantha", "Patrick", "Debra", "Raymond", "Janet", "Jack", "Carolyn", "Dennis", "Rachel",
    "Jerry", "Heather", "Tyler", "Maria", "Aaron", "Diane", "Jose", "Emma", "Henry", "Julie",
    "Douglas", "Joyce", "Adam", "Frances", "Peter", "Evelyn", "Nathan", "Joan", "Zachary", "Christina",
    "Walter", "Kelly", "Kyle", "Martha", "Harold", "Lauren", "Carl", "Victoria", "Jeremy", "Judith",
    "Keith", "Cheryl", "Roger", "Megan", "Gerald", "Alice", "Ethan", "Ann", "Arthur", "Jean",
    "Terry", "Doris", "Christian", "Andrea", "Sean", "Marie", "Lawrence", "Kathryn", "Austin", "Jacqueline",
    "Joe", "Gloria", "Noah", "Teresa", "Jesse", "Sara", "Albert", "Janice", "Bryan", "Julia",
    "Billy", "Olivia", "Bruce", "Grace", "Willie", "Rose", "Jordan", "Theresa", "Dylan", "Judy",
    "Alan", "Beverly", "Ralph", "Denise", "Gabriel", "Marilyn", "Roy", "Amber", "Juan", "Danielle",
    "Wayne", "Abigail", "Eugene", "Madison", "Logan", "Brittany", "Randy", "Diana", "Louis", "Natalie",
    "Russell", "Sophia", "Vincent", "Isabella", "Philip", "Charlotte", "Bobby", "Victoria", "Johnny", "Mia"]
    last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
    "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
    "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
    "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
    "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez",
    "Powell", "Jenkins", "Perry", "Russell", "Sullivan", "Bell", "Coleman", "Butler", "Henderson", "Barnes",
    "Gonzales", "Fisher", "Vasquez", "Simmons", "Romero", "Jordan", "Patterson", "Alexander", "Hamilton", "Graham",
    "Reynolds", "Griffin", "Wallace", "Moreno", "West", "Cole", "Hayes", "Bryant", "Herrera", "Gibson",
    "Ellis", "Tran", "Medina", "Aguilar", "Stevens", "Murray", "Ford", "Castro", "Marshall", "Owens",
    "Harrison", "Fernandez", "Mcdonald", "Woods", "Washington", "Kennedy", "Wells", "Vargas", "Henry", "Chen",
    "Freeman", "Webb", "Tucker", "Guzman", "Burns", "Crawford", "Olson", "Simpson", "Porter", "Hunter",
    "Gordon", "Mendez", "Silva", "Shaw", "Snyder", "Mason", "Dixon", "Munoz", "Hunt", "Hicks",
    "Holmes", "Palmer", "Wagner", "Black", "Robertson", "Boyd", "Rose", "Stone", "Salazar", "Fox",
    "Warren", "Mills", "Meyer", "Rice", "Schmidt", "Garza", "Daniels", "Ferguson", "Nichols", "Stephens",
    "Soto", "Weaver", "Ryan", "Gardner", "Payne", "Grant", "Dunn", "Kelley", "Spencer", "Hawkins"]

    name = random.choice(first_names) + " " + random.choice(last_names)
    age = random.randint(18, 80)
    message, condition = generate_description()
    symptoms = message.data[0].content[0].text.value
    symptoms = symptoms[symptoms.find('['):symptoms.find(']')+1]
    

    connection = sqlite3.connect('db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO patients (name, age, description, condition) VALUES (?, ?, ?, ?)', [name, age, str(symptoms), condition])
    id = cursor.lastrowid

    connection.commit()
    connection.close()

    return id

def updatePatient(id, col, data):

    connection = sqlite3.connect('db')
    cursor = connection.cursor()

    query = f'''
    UPDATE patients
    SET {col} = ?
    WHERE id = ?
    '''

    cursor.execute(query, (data, id))

    connection.commit()
    connection.close()