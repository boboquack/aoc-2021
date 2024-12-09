s=INPUT1
t=INPUT2.split('\n')
t=[j.split(' -> ') for j in t]
u={i:j for i,j in t}
for i in range(10):
    v=''
    for i in range(len(s)-1):
        j,k=s[i],s[i+1]
        if j+k in u:
            v+=u[j+k]
        else:
            v+=' '
    w=s[0]
    for i in range(len(s)-1):
        w+=v[i]
        w+=s[i+1]
    s=w
t=[s.count(i) for i in set(s)]
t.sort()
print(t[-1]-t[0])
s=INPUT1
d={}
for i in range(len(s)-1):
    if s[i:i+2] in d:
        d[s[i:i+2]]+=1
    else:
        d[s[i:i+2]]=1
for i in range(40):
    e={}
    for i in d:
        if i in u:
            p=i[0]+u[i]
            q=u[i]+i[1]
            if p in e:
                e[p]+=d[i]
            else:
                e[p]=d[i]
            if q in e:
                e[q]+=d[i]
            else:
                e[q]=d[i]
        else:
            if i in e:
                e[i]+=d[i]
            else:
                e[i]=d[i]
    d=e
v={s[-1]:1,s[0]:1}
for i in d:
    for j in i:
        if j in v:
            v[j]+=d[i]
        else:
            v[j]=d[i]
print((max(v.values())-min(v.values()))//2)
            
