k = range(1,101)
a = []
for m in k:
    for i in range(2,m):
        if m%i==0:
            break
    else:
        a.append(m)
print(a)
