s=INPUT.split(',')
s=list(map(int,s))
s.sort()
m=s[len(s)//2]
print(sum(abs(i-m) for i in s))
m=int(sum(s)/len(s))
print(min(sum(abs(i-(m+j))*(abs(i-(m+j))+1)//2 for i in s) for j in range(-3,3)))
