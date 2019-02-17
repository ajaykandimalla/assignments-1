#Write a program reverse each string from the given list and finally reverse a list.

Input_list = ["ajay" , "vamsi" , "Siva" , "hari"]
for i in range(0,len(Input_list)):
    m = Input_list[i]
    Input_list[i] = (m[-1::-1])
print(Input_list[-1::-1])
