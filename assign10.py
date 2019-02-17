'''
Write a program join each and every character from the given string with hyphen(-)
Example: 
Input_str = "PYTHON"
Output = P-Y-T-H-O-N
Note: Please Don’t use join () function.

'''

Input_str = "PYTHON"

output = Input_str[0]
for i in range(1,len(Input_str)):
    output = output +'-'+Input_str[i]
print(output)
