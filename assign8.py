'''
Write a program change the given input list by  doing rotate left.
Ex: input [4, 5, 6, 7] output [5, 6, 7, 4]
'''

list = [4,5,6,7]

list[0],list[1],list[2],list[3] = list[1],list[2],list[3],list[0]
print(list)
