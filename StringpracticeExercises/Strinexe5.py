'''To print the index of the character in a string.'''
str = "Python"
for index, char in enumerate(str):
    print("Current character",char, "at", index)

'''To convert a given string into a list of words.'''
str = "You need to keep up with this learning phase consistently."
print(str.split(' '))

'''To lowercase first n characters in a string'''
str = "RIYA TIWARI"
n = int(input("Enter the no. of first characters:"))
a = str[:n].lower(),str[n:]
print(''.join(a))

# Python code to replace, with . and vice-versa
amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)