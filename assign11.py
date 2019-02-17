1#Write a program take 10 input strings of different lengths from the user and store all the strings into a list and display only odd length strings are the output in a list format.

Input_list = []
output = []
for i in range(0,10):
    Input_list.append(input("Enter a string: "))
    if len(Input_list[i])%2!=0:
        output.append(Input_list[i])
print(output)
