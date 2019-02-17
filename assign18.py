#Write a program create a random list of length 10 and print all the elements except the elements which are divisible by 4.
import random
random_list = []
for k in range(10):
    random_list.append(random.randint(10,60))
print(random_list)
for i in random_list:
    if i%4!=0:
        print(i,end=' ')
