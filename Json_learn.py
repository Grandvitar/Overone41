import json

dict = {'first_name':['Alex', 'Pavel', 'Igor', 'Petr'],
        'last_name': ['Meleshko', 'Ivanov', 'Petrov', 'Sidorov'],
        'family_name': ['Ivanovich', 'Sergeevich', 'Olegivich', 'Petrovich'],
        'age': [38, 26, 38, 39, 36],
        'spec': ['manager', 'manager', 'finansist', 'director']}
incoding_json = json.dumps(dict, indent = 4, separators = ('', ' : '))
print(incoding_json)
with open('data_file.json', 'w') as file:
    file.write(incoding_json)
with open('data_file.json') as file:
    info = json.loads(file.read())
print(info)



