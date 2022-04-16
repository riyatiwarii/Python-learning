# Remove new line of a string.

str1='Python Exercises\n'
print(str1)
print(str1.rstrip())

# Check whether a string starts with a specific character.

string = "curiousity"
print(string.startswith("cur"))

#To display formatted text (width=50) as output.

import textwrap
sample_text = '''
  A paragraph (from Ancient Greek παράγραφος (parágraphos) 'to write beside') is a self-contained unit of discourse in 
  writing dealing with a particular point or idea. A paragraph consists of one or more sentences. Though not required by
   the syntax of any language, 
  '''
print()
print(textwrap.fill(sample_text, width=50))
print()

'''a Python program to reverse words in a string.'''

str = "I am a python programmer."
words = str.split()
words = list(reversed(words))
print(words)
print(" ".join(words))

# Doubt
# def reverse_string_words(text):
#     for line in text.split('\n'):
#         return(' '.join(line.split()[::-1]))
# print(reverse_string_words("The quick brown fox jumps over the lazy dog."))

''' a Python program to strip a set of characters from a string.'''

str = "Unleash your potential under the adverse situations, Miss Tiwari."
vowel = "aeiou"
def without_vowel(str, vowel):
    return "".join(i for i in str if i not in vowel)
print(without_vowel(str, vowel))