s=INPUT.split()
s=[list(map(int,i)) for i in s]
w=len(s[0])
h=len(s)
r=[[0]*w for i in range(h)]
r[0][0]=s[0][0]
for i in range(1,w):
    r[0][i]=r[0][i-1]+s[0][i]
for i in range(1,h):
    r[i][0]=r[i-1][0]+s[i][0]
for i in range(1,w):
    for j in range(1,h):
        r[i][j]=min(r[i-1][j],r[i][j-1])+s[i][j]
print(r[-1][-1]-s[0][0])
incr=lambda l:[i%9+1 for i in l]
s=[i+incr(i)+incr(incr(i))+incr(incr(incr(i)))+incr(incr(incr(incr(i)))) for i in s]
s=s+[incr(i) for i in s]+[incr(incr(i)) for i in s]+[incr(incr(incr(i))) for i in s]+[incr(incr(incr(incr(i)))) for i in s]
w=len(s[0])
h=len(s)
v=[[0]*w for i in range(h)]
stack=[(0,0,0)]
#cnt=0
while len(stack):
    d,x,y=stack.pop(0)
    #print(d,x,y)
    if v[x][y]:continue
    v[x][y]=1
    cnt+=1
    #if cnt%10000==0:print(cnt)
    if x==h-1 and y==w-1:
        print(d)
        break
    else:
        for dx,dy in ((0,1),(1,0),(0,-1),(-1,0)):
            if 0<=x+dx<h and 0<=y+dy<w and not v[x+dx][y+dy]:
                stack.append((d+s[x+dx][y+dy],x+dx,y+dy))
        stack.sort()
