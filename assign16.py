'''
Write a program find all even numbers from the given list.

Input_List = [18.8, "Hyd", 18, 26.9, 19,"BANG" , 26, 33.7, 25, "CHEN"]
Output = [18, 26]
'''
Input_List = [18.8, "Hyd", 18, 26.9, 19, "BANG", 26, 33.7, 25, "CHEN"]
output = []
for i in Input_List:
    if type(i)==int and i%2==0:
        output.append(i)
print(output)
