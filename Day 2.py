s=INPUT.split('\n')
l=[i.split() for i in s]
l=[(i[0],int(j)) for i,j in l]
d={'f':(1,0),'d':(0,1),'u':(0,-1)}
x,y=0,0
for i,j in l:
    q,r=d[i]
    x,y=x+q*j,y+r*j
print(x*y)

x,y,a=0,0,0
for i,j in l:
    if i=='d':a+=j
    if i=='u':a-=j
    if i=='f':x,y=x+j,y+a*j
print(x*y)
