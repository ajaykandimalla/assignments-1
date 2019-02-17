'''
Write a program find the maximum number from the given input list
Input_list = [82, 62, 61, 54, 71, 89, 75, 73]

'''
Input_list = [82, 62, 61, 54, 71, 89, 75, 73]
max_num = Input_list[0]
for i in range(1,len(Input_list)):
    if Input_list[i]>= max_num:
        max_num = Input_list[i]
print("The maximum number is: ",max_num)


min_num = Input_list[0]
for i in range(1,len(Input_list)):
    if Input_list[i]<=min_num:
        min_num = Input_list[i]
print("The minimum number is: ",min_num)
    
