#Write a program find all even number from the given input list and display output as a list format.

Input_list = range(1,101)
output = []
for i in Input_list:
    if i%2==0:
        output.append(i)
print(output)
    
