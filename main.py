import pandas as pd

path = input("Enter the path to the Excel file: ")
x = pd.read_excel(path)

branches = {

    'AA': 'ECE',
    'AB': 'Manu',
    'A1': 'Chemical',
    'A2': 'Civil',
    'A3': 'EEE',
    'A4': 'Mech',
    'A5': 'Pharma',
    'A7': 'CSE',
    'A8': 'ENI',
    'B1': 'MSc Biology',
    'B2': 'MSc Chemistry',
    'B3': 'MSc Economics',
    'B4': 'MSc Mathematics',
    'B5': 'MSc Physics'

}

students = []

for index, row in x.iterrows():
    name = row['BITS ID']
    bits_id = row['Name']

    is_dual = 0

    if bits_id[6:8] != 'PS':
        is_dual = 1

    if is_dual == 0:
        branch = branches.get(bits_id[4:6])
    elif is_dual == 1:
        branch = f'{branches.get(bits_id[4:6])} + {branches.get(bits_id[6:8])}'


    bits_email = f'f{bits_id[0:4]}{bits_id[8:13]}@pilani.bits-pilani.ac.in'

    student = {

        'Name': name,
        'BITS ID': bits_id,
        'BITS Email': bits_email,
        'Branch': branch

    }

    students.append(student)

for student in students:
    print(student)
