"""
Iterate folders and locate file
File creation
    - text file
    - json file
    - csv file
File Parsing

Assignments:
    for following assignment you have to create a new folder to store your files using code

    1. Create a list of dictionary where you store directory, add at least 10 elements and generate json file
    [{'name': 'xyz', 'phone': 12343232, 'address': 'so and so'}]

    2. Create a employee dictionary, need at least 10 elements and genereate json file
    {'<employee_no>: {'emp_id': 'emp_123232', 'name': 'emp name', 'skill_sets': ['QA', 'Python', 'SQL']}

    3. Create a employee list and generate csv file and parse it

"""

import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
print(BASE_PATH)

# ASSET_PATH = BASE_PATH + '/'  + 'assets' # Not recommended
ASSET_PATH = os.path.join(BASE_PATH, 'assets')

if not os.path.exists(ASSET_PATH):
    os.makedirs(ASSET_PATH)

TEXT_FILE_PATH = os.path.join(ASSET_PATH, 'text.txt')

# _file = open(TEXT_FILE_PATH, 'w')
# _file.write('This is my first line\n')
# _file.write('This is my second line.\n')
# _file.close()


# with open(TEXT_FILE_PATH, 'w') as _file:
#     _file.write('This is my first line\n')
#     _file.write('This is my second line.\n')

# if os.path.exists(TEXT_FILE_PATH):
#     with open(TEXT_FILE_PATH, 'r') as _file:
#         # for i in _file.readlines():
#         #     print(i, end="")
#
#         # print(_file.readline(), end='')
#         # print(_file.readline(), end='')


# _data = {
#     123: {
#         'name': 'pavan',
#         'addresss': {
#             'line1': 'address line 1',
#             'line2': 'address line 2',
#             'line3': 'address line 3',
#             'city': 'Pune'
#         },
#         'contact': '12345688422',
#         'email': 'pavan@pavan.com'
#     },
#     124: {
#         'name': 'Jimmy',
#         'addresss': {
#             'line1': 'address line 1',
#             'line2': 'address line 2',
#             'line3': 'address line 3',
#             'city': 'Pune'
#         },
#         'contact': '12345688422',
#         'email': 'jimmy@jimmy.com'
#     }
# }

# import json
# JSON_FILE_PATH = os.path.join(ASSET_PATH, 'my_json.json')

# with open(JSON_FILE_PATH, 'w') as _file:
#     json.dump(obj=_data, fp=_file)

# with open(JSON_FILE_PATH, 'r') as _file:
#     json_data = json.load(_file)
#
#     print(json_data.get('123'))

_data = [
    ['no', 'name', 'age', 'contact'],
    [1, 'Pavan  Maradia', 31, 9840548303],
    [2, 'Jimmy', 33, 9343923893],
    [3, 'Kirti', '-', 94345443434],
    [4, 'Seema', '-', 93345443434],
    [5, 'Vaibhavi', '-', 94346743434]
]

import csv
CSV_FILE = os.path.join(ASSET_PATH, 'my_csv.csv')
with open(CSV_FILE, 'w') as _file:
    csv_writer = csv.writer(_file)
    csv_writer.writerows(_data)

with open(CSV_FILE, 'r') as _file:
    csv_read = csv.reader(_file)
    for i in csv_read:
        print(i)