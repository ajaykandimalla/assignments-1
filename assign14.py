'''
WAP replace each string from the given list with the same string which is repeated with length of the string. 
Example: 
Input = ["A", "AB", "ABC", "ABCD"]
Output = ["A", "ABAB","ABCABCABC","ABCDABCDABCDABCD"] 
'''
Input = ["A", "AB", "ABC", "ABCD"]
for i in range(0,len(Input)):
    Input[i] = (Input[i]*len(Input[i]))
print(Input)
