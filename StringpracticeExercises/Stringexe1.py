'''A Python program to count the number of characters (character frequency) in a string.'''
#first way
from collections import Counter
a_string = "google.com"
res = Counter(a_string)
print(str(res))
# second way
a_string = "google.com"
def count_char(a_string):
    dict = {}
    for i in a_string:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(count_char(a_string))

''' Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string. '''

samplestr = "w3"
def joinchars(samplestr):
    if len(samplestr) > 1:
        operations = (samplestr[:2] + samplestr[-2:])
    else:
        operations = ""
    return operations
print(joinchars(samplestr))

'''Write a Python program to get a string from a given string where all occurrences of its first char have been
 changed to '$', except the first char itself'''

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))