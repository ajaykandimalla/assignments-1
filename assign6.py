'''
WAP print all duplicated values in descending order from the given input list. 
Input_list = [401, 403, 409, 403, 453, 402, 438, 401, 444]
Output: 
Duplicated elements: [403, 401]
'''
Input_list = [401, 403, 409, 403, 453, 402, 438, 401, 444]
k =[]
Input_list.sort()
print(Input_list)

for i in range(0,len(Input_list)-1):
    if Input_list[i] ==Input_list[i+1]:
        k.append(Input_list[i])
print(k)
    
