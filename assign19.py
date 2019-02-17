'''
Write a program convert the following list to a dictionary. 
X = [("A", 65), ("B", 66), ("C" 67), ("D", 68)]
Note: Please don’t use dict() function. 
'''

X = [("A", 65), ("B", 66), ("C", 67), ("D", 68)]
dict = {}
for i in range(0,len(X)):
    dict[X[i][0]] = X[i][1]
print(dict)
       
