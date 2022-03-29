row = int(input("Enter the no. of rows for your star pattern:\n"))
boolean = bool(int(input("Enter any of the two numbers: 0 or 1\n")))
if boolean == 0:
    print("True")
    for i in range(row):
        for j in range(i+1):
            print("*",end=" ")
        print()
elif boolean == 1:
    print("False")
    for i in range(row):
        for j in range(row-i):
            print("*",end=" ")
        print()

row = int(input("Enter the no. of rows for your star pattern:\n"))
for i in range(row):
    for j in range(row):
        print("$", end="   ")
    print()

row = int(input("Enter the no. of rows for your star pattern:\n"))
for i in range(row):
     for j in range(i+1):
         print(" ",end=" ")
         for j in range(row-i):
             print("*",end=" ")
     print()



























