s=INPUT.split()
t=0
d={i:j for i,j in zip('<({[','>)}]')}
z={i:j for i,j in zip('>)}]',[25137,3,1197,57])}
r=[]
for i in s:
    stack=[]
    for j in i:
        if j in d:stack.append(j)
        else:
            q=stack.pop()
            if d[q]!=j:
                t+=z[j]
                break
    else:
        r.append(i)
print(t)
y={i:j for i,j in zip('([{<',[1,2,3,4])}
w=[]
for i in r:
    stack=[]
    for j in i:
        if j in d:stack.append(j)
        else:stack.pop()
    a=0
    for i in stack[::-1]:
        a*=5
        a+=y[i]
    w.append(a)
w.sort()
print(w[len(w)//2])
