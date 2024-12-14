import json
a = [["1", "ali"],2,3]
with open('test.txt', 'w') as f:
    json.dump(a, f)

#Now read the file back into a Python list object
with open('test.txt', 'r') as f:
    a = json.load(f)
print(a)
print(a[0][1])