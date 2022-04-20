''' Write a Python program to count the occurrences of each word in a given sentence. '''

samplestr = "Riya"
newstr = ""
for i in range(len(samplestr)):
    if i % 2 == 0:
        newstr = newstr+samplestr[i]
print(newstr)

''' Write a Python program to count the occurrences of each word in a given sentence. '''

sample = "Big black bug bit a big black dog on his big black nose"
sample = sample.lower()
def word_count(str):
    words = sample.split(" ")
    count = dict()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
print(word_count(sample))




