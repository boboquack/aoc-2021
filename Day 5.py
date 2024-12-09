s=INPUT.split('\n')

q=[[0]*1000 for i in range(1000)]
for i in s:
    a,b=i.split(' -> ')
    c,d=a.split(',')
    e,f=b.split(',')
    c,d,e,f=map(int,[c,d,e,f])
    if c==e:
        for i in range(min(d,f),max(d,f)+1):q[c][i]+=1
    elif d==f:
        for i in range(min(c,e),max(c,e)+1):q[i][d]+=1
print(sum(sum(i>1 for i in j) for j in q))

q=[[0]*1000 for i in range(1000)]
for i in s:
    a,b=i.split(' -> ')
    c,d=a.split(',')
    e,f=b.split(',')
    c,d,e,f=map(int,[c,d,e,f])
    if c==e:
        for i in range(min(d,f),max(d,f)+1):q[c][i]+=1
    elif d==f:
        for i in range(min(c,e),max(c,e)+1):q[i][d]+=1
    elif (c<e and d<f) or (c>e and d>f):
        for i in range(min(c,e),max(c,e)+1):q[i][i+min(d,f)-min(c,e)]+=1
    else:
        for i in range(min(c,e),max(c,e)+1):q[i][max(d,f)-i+min(c,e)]+=1
print(sum(sum(i>1 for i in j) for j in q))
