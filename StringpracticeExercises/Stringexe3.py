samplestr = "Riya"
newstr = ""
for i in range(len(samplestr)):
    if i % 2 == 0:
        newstr = newstr+samplestr[i]
print(newstr)

string = "big black bug bit a big black dog on his big black nose";

# # Split the string into words using built-in function
# words = string.split(" ");
#
# print("Duplicate words in a given string : ");
# for i in range(0, len(words)):
#     count = 1;
#     for j in range(i+1, len(words)):
#         if (words[i] == (words[j])):
#             count = count + 1;
#             # Set words[j] to 0 to avoid printing visited word
#             words[j] = "0";
#
#             # Displays the duplicate word if count is greater than 1
#     if (count > 1 and words[i] != "0"):
#         print(words[i]);