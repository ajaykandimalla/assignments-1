'''
Write a program take input strings of equal length and the length of strings should be greater than 5 and display the output by combining last three characters from the 1st string with first three characters from the second string. 
Example: Input_Str1 = "AJAYKRISHNA"
                  Input_Str2 = "PROGRAMMING"
                  Output = HONPRO
'''

str1 = "AJAYKRISHNA"
str2 = "PROGRAMMING"

str = str1[-3:]+str2[:3]
print(str)
