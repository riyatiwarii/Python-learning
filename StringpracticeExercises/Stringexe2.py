''' Write a Python program to get a single string from two given strings, separated by a space and
swap the first two characters of each string.'''
a = "abc"
b = "xyz"
def swapstr(a, b):
    new_a = b[:2]+a[2:]
    new_b = a[:2]+b[2:]
    operator = new_a+" "+new_b
    return operator
print(swapstr(a,b))

'''
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
'''
str = "abc"
def replace_char(str):
  if len(str) >= 3:
    if str[-3:] == "ing":
       return str+"ly"
    else:
      return str+"ing"
  else:
    return str
print(replace_char(str))

'''
Write a Python function that takes a list of words and return the longest word and the length of the
longest one.'''
samplelist = ["Phenomenal","Gorgeous","Dazzling","Ravishing","Pulchritudinous"]
long_samplelist = max(samplelist, key=len)
print(long_samplelist)
print(len(long_samplelist))

'''
Write a Python program to change a given string to a new string where the first and last chars 
have been exchanged.
'''
samplestr = "Riya"
a = samplestr[-1:]
b = a.capitalize()
c = samplestr[:1]
d = c.lower()
new_str = b +samplestr[1:-1]+ d
print(new_str)
