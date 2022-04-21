# ''' to count and display the vowels of a given text'''
# str = 'Favourite'
# vowel = 'aeiouAEIOU'
# def countvowel(str):
#     return (len([char for char in str if char in vowel]))
# print(countvowel(str))
#
# '''to split a string on the last occurrence of the delimiter.'''
# str1 = "r,i,y,a,t,i,w,a,r,i"
# print(str1.rsplit(',',2))

'''a Python program to find the first non-repeating character in given string.'''

str1 = "abcdabc"
def nonrepeated(str1):
    freq = {}
    for char in str1:
        freq[char] = freq.get(char,0)+1
    for i in str1:
        if freq[i] == 1:
            return i
    return -1
print(nonrepeated(str1))


