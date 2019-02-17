'''
WAP find the average of given list of elements representing a grade of student.
grades = [84, 84, 93, 78, 86, 73]

'''
grades = [84, 84, 93, 78, 86, 73]

sum = 0
for i in grades:
    sum = sum+i
print("The avg of the student is: " , sum/len(grades))
