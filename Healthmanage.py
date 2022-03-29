# Health Management System
# lock or retrive
# 3 clients - Harry, Rohan and Hammad
# Total 6 file
# 3 file food lock
# 3 file excercise lock
# write a function that when executed takes as input client name
# one more function to retrive exercise or food for any client
# a = int(input("lock or retrive 1 for lock & 2 for retrive\n"))
# c = int(input("1 for Harry, 2 for Rohan & 3 for Hammad\n"))
# fe = int(input("food or exercise 1 for food & 2 for excercise\n"))
print("Health Management System")
clientname = int(input("Enter 1 for Harry or  2 for Rohan or 3 for Hammad\n"))
lockret = int(input("Enter 1 for locking data or 2 for retrieving data\n"))
foodexe = int(input("Enter 1 for food or 2 for exercise\n"))
if clientname == 1:
    if lockret == 1:
        if foodexe == 1:
            f = open("Harryfood.txt","a")
            food = input("Enter food to add\n")
            f.write( food + "\n")
            print("food entered successfully.")
            f.close()
        elif foodexe == 2:
            f = open("Harryexe.txt","a")
            exercise = input("Enter exercise to add\n")
            f.write(exercise + "\n")
            print("Exercise entered successfully.")
        else:
            print("enter right choice")
    elif lockret == 2:
        if foodexe == 1:
            f = open("Harryfood.txt","r")
            for i in f:
                print(i, end="")
            f.close()
        elif foodexe == 2:
            f = open("Harryexe.txt", "r")
            for i in f:
                print(i, end="")
            f.close()
        else:
            print("enter right choice")
if clientname == 2:
    if lockret == 1:
        if foodexe == 1:
            f = open("Rohanfood.txt","a")
            food = input("Enter food to add\n")
            f.write( food + "\n")
            print("food entered successfully.")
            f.close()
        elif foodexe == 2:
            f = open("Rohanexe.txt","a")
            exercise = input("Enter exercise to add\n")
            f.write(exercise + "\n")
            print("Exercise entered successfully.")
        else:
            print("enter right choice")
    elif lockret == 2:
        if foodexe == 1:
            f = open("Rohanfood.txt","r")
            for i in f:
                print(i, end="")
            f.close()
        elif foodexe == 2:
            f = open("Rohanexe.txt", "r")
            for i in f:
                print(i, end="")
            f.close()
        else:
            print("enter right choice")
if clientname == 3:
    if lockret == 1:
        if foodexe == 1:
            f = open("Hammadfood.txt","a")
            food = input("Enter food to add\n")
            f.write(food + "\n")
            print("food entered successfully.")
            f.close()
        elif foodexe == 2:
            f = open("Hammadexe.txt","a")
            exercise = input("Enter exercise to add\n")
            f.write(exercise + "\n")
            print("Exercise entered successfully.")
        else:
            print("enter right choice")
    elif lockret == 2:
        if foodexe == 1:
            f = open("Hammadfood.txt","r")
            for i in f:
                print(i, end="")
            f.close()
        elif foodexe == 2:
            f = open("Hammadexe.txt", "r")
            for i in f:
                print(i, end="")
            f.close()
        else:
            print("enter right choice")

