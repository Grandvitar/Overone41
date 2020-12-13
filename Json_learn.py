import json
with open('data_file.json') as file:
    info = json.loads(file.read())
prof = []
for i in range(len(info)):
    if info[i].get("profession") not in prof:
        prof.append(info[i].get("profession"))
print(prof)
for i in range(len(prof)):
    s = prof[i]
    m = []
    for k in range(len(info)):
        if info[k].get("profession") == prof[i]:
            m.append(info[k])
            j = json.dumps(m, indent = 4)
            with open(f'{s}.json', 'w') as file:
                file.write(j)






