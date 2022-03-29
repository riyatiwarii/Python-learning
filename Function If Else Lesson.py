Age = int(input("What's your age?  "))
if Age < 7 or Age > 100:
    print("This is not a logical age.")
elif Age < 18:
    print("You are not eligible to drive.")
elif Age > 18:
    print("You are eligible to drive.")
else:
    print("We will think about it.")

