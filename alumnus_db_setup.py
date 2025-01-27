import json

# uploading json
with open('alumnus.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# getting rid of " and ' inside values of type str
keys = data[0].keys()
for i in range(len(data)):
    for key in keys:
        if isinstance(data[i][key], str):
            data[i][key] = data[i][key].replace("'", " ")
            data[i][key] = data[i][key].replace('"', " ")

# creating a query
with open('query.txt', 'w', encoding='utf-8') as file:
    file.write('''INSERT INTO alumnus (info)
VALUES''')
    for i in range(len(data)):
        s = data[i].__str__().replace("'", '"')
        if i == 0:
            file.write(f"('{s}'),\n")
        elif i < len(data) - 1:
            file.write(f"{' ' * 6}('{s}'),\n")
        else:
            file.write(f"{' ' * 6}('{s}');\n")
