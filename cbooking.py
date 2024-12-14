import cdata
import json
################################### Functions ##########################
# def readFilmsData():
#     with open('filmsdata.txt', 'r') as f:
#         filmsData = json.loads(f.read())
# def writeFilmsData(filmsData):
#     with open('filmsdata.txt', 'w') as f:
#         filmsData = json.dump(filmsData, f)


# def readUsersData():
#     with open('usersData.txt', 'r') as f:
#         filmsData = json.loads(f.read())
# def writeUsersData(usersData):
#     with open('usersData.txt', 'w') as f:
#         usersData = json.dump(usersData, f)


   
vendorData = []
usersData = []
filmsData = []

isVendor = False
def readvendorData():
    with open('vendor.txt', 'r') as f:
        global vendorData 
        vendorData = json.loads(f.read())
        
def addFilm():
    Name = input("Enter the film Name: ")
    Desc = input("Enter the film Desc: ")
    seatsNumber = input("Enter the number of seats: ")
    Id = input("Enter the film id: ")
    filmData = {"Name": Name, "Desc": Desc, "seatsNumber": seatsNumber, "Id": Id}
    filmsData.append(filmData)
    writeFilmsData()
    print("Your Film is successfully added")


def removeFilm():
    global filmsData
    Name = input("Enter the film Name you want to delete: ")
    isFound = False
    for index, film in enumerate(filmsData):
        if(film['Name']==Name):
            isFound = True
            filmsData.pop(index)
    if(isFound):
        print("TheFilm is successfully removed")
        writeFilmsData()
    else:
        print("This film is not in the available list")
    
    


def vendorScenario():
    names = []
    for film in filmsData:
        names.append(film['Name'])
    print("Available Movies are :"+str(names))
    addFilmOption = input("Do want to add new film to films list? (Yes/No) ")
    while addFilmOption == "Yes":
        addFilm()
        addFilmOption = input("Do want to add new film to films list? (Yes/No) ")
    removeFilmOption = input("Do want remove a film from films list? (Yes/No) ")
    while removeFilmOption == "Yes":
        removeFilm()
        removeFilmOption = input("Do want remove a film from films list? (Yes/No) ")

def userScenario():
    global filmsData
    names = []
    print("1111")
    for film in filmsData:
        names.append(film['Name'])
    print("Available Movies are :"+str(names))
    
    movieBooked = False
    movieFound = False
    while movieBooked == False:
        movieName = input("Which movie do you want to watch? " + str(names) + " :")
        for index,film in enumerate(filmsData):
            if(movieName == film['Name']):
                movieFound = True
                print("Movie Description is : " + str(film['Desc']))
                bookConfirmation = input("Do you want to book a ticket? (Yes/No)")
                if(bookConfirmation=="Yes"):
                    seatsNumber = int(filmsData[index]['seatsNumber'])
                    if(seatsNumber == 0):
                        print("This Movie is not available")
                        movieBooked = False

                    else:
                        seatsNumber = seatsNumber - 1
                        print("You successfully booked a ticket for "+ str(movieName) + " Film")
                        print("Your seat number is " + film['seatsNumber'])
                        movieBooked = True
                        print(seatsNumber)
                        filmsData[index] = {"Name": filmsData[index]["Name"], "Desc": filmsData[index]["Desc"], "seatsNumber": str(seatsNumber), "Id": filmsData[index]["Id"]}
                        if(seatsNumber==0):
                            filmsData.pop(index)
                        writeFilmsData()
                        break
        if(movieFound==False):
            print("This Movie is not in the available movies list")




    

    







def readFilmsData():
    with open('filmsdata.txt', 'r') as f:
        global filmsData
        filmsData = json.loads(f.read())
def writeFilmsData():
    with open('filmsdata.txt', 'w') as f:
        global filmsData
        filmsData = json.dump(filmsData, f)


def readUsersData():
    with open('usersData.txt', 'r') as f:
        global usersData
        usersData = json.loads(f.read())
def writeUsersData():
    with open('usersData.txt', 'w') as f:
        global usersData
        usersData = json.dump(usersData, f)
                    # vendor data


def checkType():
    global usersData
    global filmsDatar
    register = input("Do you want to register or login? (register/login)")

    if(register=='login'):
    
        userFound = False
        
        while userFound == False:
            userEmail= input("what is your email adress ? ")
            userPass = input("what is your password ? ")
            
            
            if userEmail==vendorData['email'] and userPass==vendorData['password'] :
                userFound = True
                global isVendor
                isVendor = True
                vendorScenario()
            else:
                for index , user in enumerate(usersData):
                    if(userEmail == user['email'] and userPass == user['password']):
                        userFound = True
                        userScenario()
                        break
            if(userFound == False):
                print("Incorrect email or password")
    else:
        print("Now enter your data to register")
        userEmail= input("what is your email adress ? ")
        userPass = input("what is your password ? ")
        userName = input("what is your Name ? ")
        userNationalId = input("what is your national id ? ")
        userPhoneNumber = input("what is your phone number ? ")
        userData = {"name": userName, "email": userEmail, "id": len(usersData), "password": userPass, "nationalid": userNationalId, "phoneNumber": userPhoneNumber}
        usersData.append(userData)
        
        writeUsersData()

                

        
 
readvendorData()
readUsersData()
readFilmsData()
checkType()
if(isVendor):
    print("is vendor")
else:
    print("not vendor")















































































































# def choose_movie():
#             global coll_name
#             global coll_email
#             global coll_pass
#             global coll_id
#             global coll_phone
#             global coll_movie
#             global coll_national
            
#             global conf
#             global numm

#             global movie

#             global guest_names
#             global guest_id
#             global guest_email
#             global guest_national
#             global guest_pass
#             global guest_phone

#             global film1_des
#             global film2_des
#             global film3_des
#             global film1
#             global film2
#             global film3
#             global film1_seats
#             global film2_seats
#             global film3_seats
#             global film1_id
#             global film2_id
#             global film3_id



#             print("hello "+ coll_name +" wellcome to our cinema!")
#             movie = input("which movie do you want to enter watch from these ( split, thor, interstellar ) ?" )
#             if str(movie).lower() == film1:
#                 if film1_seats >= 1 :
#                     print("there are available seats for this movie")
#                     print("Movie Description : " + film1_des)
#                     ask = input("are you ready to enter the movie or you want to change it ? (YES/NO)")
#                     if ask.upper() == "YES" :
#                         film1 = film1_seats - 1
#                         print("OK Sir, We wish you an enjoyable movie,your movie id " + film1_id + " your seat number is " + str(20-film1_seats)+ " enjoy !!")
#                     else :
#                         choose_movie()
#                 elif film1_seats <= 0 :
#                     print("sorry, this movie is fully booked now !")
#                     xz = input("do you want to change the movie ? (YES/NO)")
#                     if xz.upper() == "YES":
#                         choose_movie()
#                     elif xz.upper == "NO":
#                         print("thanks for visiting us!")
#                         pass
#                     else:
#                         print("sorry you have entered something wrong, try again!")
#                         pass
#             elif str(movie).lower() == film2 :
#                 if film2_seats >= 1 :
#                     print("there are available seats for this movie")
#                     print("Movie Description : " + film2_des)
#                     ask = input("are you ready to enter the movie or you want to change it ? (YES/NO)")
#                     if ask.upper() == "YES" :
#                         film2 = film2_seats - 1
#                         print("OK Sir, We wish you an enjoyable movie," + film2_id + " your seat number is " + str(20-film2_seats)+ " enjoy !!")
#                     else :
#                         choose_movie()
#                 elif film2_seats <= 0 :
#                     print("sorry, this movie is fully booked now !")
#                     zy = input("do you want to change the movie ? (YES/NO)")
#                     if zy.upper() == "YES":
#                         choose_movie()
#                     elif zy.upper == "NO":
#                         print("thanks for visiting us!")
#                         pass
#                     else:
#                         print("sorry you have entered something wrong, try again!")
#                         pass
#             elif str(movie).lower() == film3 :
#                 if film3_seats >= 1 :
#                     print("there are available seats for this movie")
#                     print("Movie Description : " + film3_des)
#                     ask = input("are you ready to enter the movie or you want to change it ? (YES/NO)")
#                     if ask.upper() == "YES" :
#                         film3 = film3_seats - 1
#                         print("OK Sir, We wish you an enjoyable movie," + film3_id + " your seat number is " + str(20-film3_seats)+ " enjoy !!")
#                     else :
#                         choose_movie()
#                 elif film3_seats <= 0 :
#                     print("sorry, this movie is fully booked now !")
#                     xy = input("do you want to change the movie ? (YES/NO)")
#                     if xy.upper() == "YES":
#                         choose_movie()
#                     elif xy.upper == "NO":
#                         print("thanks for visiting us!")
#                         pass
#                     else:
#                         print("sorry you have entered something wrong, try again!")
#                         pass
#             else :
#                 print("sorry, you have entered something wrong, please try again !")
#                 pass






""""

#                     # vendor data

#data = cdata


#vendor_id = data.vendor_id
#vendor_name = data.vendor_name
#vendor_email = data.vendor_email
#vendor_pass = data.vendor_pass




#############################################

                                                    # film data #
#film1 = data.film1
#film2 = data.film2
#film3 = data.film3

#film1_des = data.film1_des
#film2_des = data.film2_des
#film3_des = data.film3_des

#f1 = cdata.film1_seatsd
#f2 = cdata.film2_seatsd
#f3 = cdata.film3_seatsd

#film1_seats = f1
#film2_seats = f2
#film3_seats = f3

#film1_id = data.film1_id
#film2_id = data.film2_id
#film3_id = data.film3_id

###################################################
# guest Data


#guest_names = data.guest_names

#guest_id = data.guest_id

#guest_pass = data.guest_pass

#guest_email = data.guest_email

#guest_phone = data.guest_phone



#guest_national = data.guest_national





#coll_name = None
coll_email = None
coll_pass = None
coll_id = None
coll_phone = None
coll_movie = None
coll_national = None

conf = None
numm = 0






def loopconf():
    global coll_name
    global coll_email
    global coll_pass
    global coll_id
    global coll_phone
    global coll_movie
    
    global conf
    global numm

    global guest_names
    global guest_id
    global guest_email
    global guest_national
    global guest_pass
    global guest_phone

    while numm < 80 :
        if coll_name == guest_names[numm] and coll_email == guest_email[numm] and coll_pass == guest_pass[numm] and coll_id == guest_id[numm] and coll_national == guest_national[numm] and coll_phone == guest_phone[numm] :
            conf = True
            break
        else :
            numm = numm + 1
            
movie = None


def mixed_question():
    global coll_name
    global coll_email
    global coll_pass
    global coll_id
    global coll_phone
    global coll_movie
        
    global conf
    global numm

    global guest_names
    global guest_id
    global guest_email
    global guest_national
    global guest_pass
    global guest_phone

    coll_name = input("hello, what is your name ?")
    coll_email = input("what is your email adress ?")
    coll_pass = input("what is your password ?")
    coll_id = input("what is your id ?")


def special_questions():
    global coll_name
    global coll_email
    global coll_pass
    global coll_id
    global coll_phone
    global coll_movie
    global coll_national
    
    global conf
    global numm

    global movie

    global guest_names
    global guest_id
    global guest_email
    global guest_national
    global guest_pass
    global guest_phone


    coll_phone = input("what is your phone number ?")
    coll_national = input("what is your national id ?")





def choose_movie():
            global coll_name
            global coll_email
            global coll_pass
            global coll_id
            global coll_phone
            global coll_movie
            global coll_national
            
            global conf
            global numm

            global movie

            global guest_names
            global guest_id
            global guest_email
            global guest_national
            global guest_pass
            global guest_phone

            global film1_des
            global film2_des
            global film3_des
            global film1
            global film2
            global film3
            global film1_seats
            global film2_seats
            global film3_seats
            global film1_id
            global film2_id
            global film3_id
            global f1
            global f2
            global f3

            movie = input("which movie do you want to enter watch from these ( Split, Thor, Interstellar ) ?" )
            if str(movie).capitalize() == film1:
                if film1_seats >= 1 :
                    print("there are available seats for this movie")
                    print("Movie Description : " + film1_des)
                    ask = input("are you ready to enter the movie or you want to change it ? (YES/NO)")
                    if ask.upper() == "YES" :
                        film1_seats =film1_seats - 1
                        print("OK Sir, We wish you an enjoyable movie,your movie id " + film1_id + " your seat number is " + str(20-film1_seats)+ " enjoy !!")
                    else :
                        choose_movie()
                elif film1_seats <= 0 :
                    print("sorry, this movie is fully booked now !")
                    xz = input("do you want to change the movie ? (YES/NO)")
                    if xz.upper() == "YES":
                        choose_movie()
                    elif xz.upper() == "NO":
                        print("thanks for visiting us!")
                        
                    else:
                        print("sorry you have entered something wrong, try again!")
                        
            elif str(movie).capitalize() == film2 :
                if film2_seats >= 1 :
                    print("there are available seats for this movie")
                    print("Movie Description : " + film2_des)
                    ask = input("are you ready to enter the movie or you want to change it ? (YES/NO)")
                    if ask.upper() == "YES" :
                        film2_seats = film2_seats - 1
                        print("OK Sir, We wish you an enjoyable movie," + film2_id + " your seat number is " + str(20-film2_seats)+ " enjoy !!")
                    else :
                        choose_movie()
                elif film2_seats <= 0 :
                    print("sorry, this movie is fully booked now !")
                    zy = input("do you want to change the movie ? (YES/NO)")
                    if zy.upper() == "YES":
                        choose_movie()
                    elif zy.upper() == "NO":
                        print("thanks for visiting us!")
                        
                    else:
                        print("sorry you have entered something wrong, try again!")
                        
            elif str(movie).capitalize() == film3 :
                if film3_seats >= 1 :
                    print("there are available seats for this movie")
                    print("Movie Description : " + film3_des)
                    ask = input("are you ready to enter the movie or you want to change it ? (YES/NO)")
                    if ask.upper() == "YES" :
                        film3_seats = film3_seats - 1
                        print("OK Sir, We wish you an enjoyable movie," + film3_id + " your seat number is " + str(20-film3_seats)+ " enjoy !!")
                    else :
                        choose_movie()
                elif film3_seats <= 0 :
                    print("sorry, this movie is fully booked now !")
                    xy = input("do you want to change the movie ? (YES/NO)")
                    if xy.upper() == "YES":
                        choose_movie()
                    elif xy.upper() == "NO":
                        print("thanks for visiting us!")
                        
                    else:
                        print("sorry you have entered something wrong, try again!")
                        
            else :
                print("sorry, you have entered something wrong, please try again !")
                





# mixed_question()
# if coll_name == vendor_name and coll_email == vendor_email and coll_pass == vendor_pass and coll_id == vendor_id :
#     print("###############################################################")
#     print("wellcome SIR, have a nice day")
#     print("the available seats for " + film1 + " are " + str(film1_seats))
#     print("the available seats for " + film2 + " are " + str(film2_seats))
#     print("the available seats for " + film3 + " are " + str(film3_seats))
#     print("###############################################################")
# elif coll_name in guest_names and coll_email in guest_email and coll_pass in guest_pass and coll_id in guest_id :
#     special_questions()
#     if coll_phone in guest_phone and coll_national in guest_national :
#         loopconf()
#         if conf == True :
#             conf = None
#             numm = 0
#             print("hello "+ coll_name +" wellcome to our cinema!")
#             choose_movie()
#         else :
#             print("sorry, your data are not correct please try again!")
#     else :
#         print("sorry you have entered something wrong, please try again !")


# print(film1_seats)
# print(film2_seats)
# print(film3_seats)

"""


































































# guest_phone = []
# y = 0
# z = None
# i = 0


# def num_creator( ):
#     global guest_phone
#     global y
#     global z
#     global i
#     while y < 80:
#         x = random.randint(1,4)
#         if x == 1 :
#             z = "010"
#             while i < 8 :
#                 a = random.randint(0,9)
#                 z = z +  str(a)
#                 i = i + 1
#             i = 0
#         elif x == 2 :
#             z = "011"
#             while i < 8 :
#                 a = random.randint(0,9)
#                 z = z +  str(a)
#                 i = i + 1
#             i = 0

#         elif x == 3 :
#             z = "012"
#             while i < 8 :
#                 a = random.randint(0,9)
#                 z = z +  str(a)
#                 i = i + 1
#             i = 0

#         elif x == 4 :
#             z = "015"
#             while i < 8 :
#                 a = random.randint(0,9)
#                 z = z +  str(a)
#                 i = i + 1
#             i = 0
#         guest_phone.append(z)
#         y = y + 1 

# num_creator()

# print(guest_phone)






