s=INPUT.split()
l=[int(i) for i in s]
print(sum(i<j for i,j in zip(l,l[1:])))
print(sum(i<j for i,j in zip(l,l[3:])))
