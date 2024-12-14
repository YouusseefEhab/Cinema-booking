import json
a = [1,2,3]
with open('test.txt', 'w') as f:
    f.write(json.dumps(a))

#Now read the file back into a Python list object
with open('test.txt', 'r') as f:
    a = json.loads(f.read())
print(a)