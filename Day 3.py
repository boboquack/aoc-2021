s=INPUT.split()
g=''
for i in zip(*s):
    if i.count('1')*2>=len(s):g+='1'
    else:g+='0'
e=int(g.replace('0','a').replace('1','0').replace('a','1'),2)
g=int(g,2)
print(g*e)
t=s[:]
i=-1
while len(t)>1:
    i+=1
    v=[j[i] for j in t]
    if v.count('1')*2>=len(t):
        t=[j for j in t if j[i]=='1']
    else:
        t=[j for j in t if j[i]=='0']
u=s[:]
i=-1
while len(u)>1:
    i+=1
    v=[j[i] for j in u]
    if v.count('1')*2>=len(u):
        u=[j for j in u if j[i]=='0']
    else:
        u=[j for j in u if j[i]=='1']
print(int(t[0],2)*int(u[0],2))
