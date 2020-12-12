import json
with open('data_file.json') as file:
    info = json.loads(file.read())
professions = [] #это делаю для того, чтобы вытянуть все профессии из файла
for i in range(len(info)):
    professions.append(info[i].get("profession"))
professions = list(set(professions))
print(professions) #конец блока, можно и без него
for i in range(len(info)):
    if info[i].get("profession") == 'engineer':
        engineer.append(info[i])
    elif info[i].get("profession") == 'director':
        director.append(info[i])
    elif info[i].get("profession") == 'manager':
        manager.append(info[i])
engineer_json = json.dumps(engineer, indent = 4)
manager_json = json.dumps(manager, indent = 4)
director_json = json.dumps(director, indent = 4)
with open('manager.json', 'w') as file:
    file.write(manager_json)
with open('engineer.json', 'w') as file:
    file.write(engineer_json)
with open('director.json', 'w') as file:
    file.write(director_json)






