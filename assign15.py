#Take two input strings from the user and concatenate two given strings by omitting the first character.

str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
str = str1[1:] + str2[1:]
print(str)
