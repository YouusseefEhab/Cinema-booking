import json


filmsData = []
def readFilmsData():
    with open('filmsdata.txt', 'r') as f:
        filmsData = json.loads(f.read())
def writeFilmsData(filmsData):
    with open('filmsdata.txt', 'w') as f:
        filmsData = json.dump(filmsData, f)

def vendorData():
    with open('vendor.txt', 'r') as f:
        filmsData = json.loads(f.read())


def readUsersData():
    with open('usersData.txt', 'r') as f:
        filmsData = json.loads(f.read())
def writeUsersData(usersData):
    with open('usersData.txt', 'w') as f:
        usersData = json.dump(usersData, f)
vendorData = []
filmsData = [
    {'Name':'Thor','Desc':'action','seatsNumber':'20','id':'1234'},
    {'Name':'Split','Desc':'action','seatsNumber':'20','id':'1234'},
    {'Name':'Intersteller','Desc':'science fiction','seatsNumber':'20','id':'1234'},
    ]
usersData = [
    {'name':'Thor','email':'action','id':'20','password':'1234','nationalid':'1234','phoneNumber':'1234'},
    {'name':'Thor','email':'action','id':'20','password':'1234','nationalid':'1234','phoneNumber':'1234'},
]
readFilmsData()
print(filmsData)

list1 = [1,2,3,4,5,6,67]
list1.pop(3)
print(list1)
