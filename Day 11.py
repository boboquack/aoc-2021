s='''5433566276
6376253438
8458636316
6253254525
7211137138
1411526532
5788761424
8677841514
1622331631
5876712227'''.split()
o=[list(map(int,i)) for i in s]
h=len(s)
w=len(s[0])
cnt=0
for step in range(100):
    fgrid=[[0]*w for i in range(h)]
    over9=[]
    for i in range(h):
        for j in range(w):
            o[i][j]+=1
            if o[i][j]>9:
                fgrid[i][j]=1
                over9.append((i,j))
    while len(over9):
        t,u=over9.pop()
        cnt+=1
        for dt,du in ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)):
            if 0<=t+dt<h and 0<=u+du<w:
                o[t+dt][u+du]+=1
                if o[t+dt][u+du]>9 and fgrid[t+dt][u+du]==0:
                    fgrid[t+dt][u+du]=1
                    over9.append((t+dt,u+du))
    for i in range(h):
        for j in range(w):
            if fgrid[i][j]:o[i][j]=0
print(cnt)
s='''5433566276
6376253438
8458636316
6253254525
7211137138
1411526532
5788761424
8677841514
1622331631
5876712227'''.split()
o=[list(map(int,i)) for i in s]
h=len(s)
w=len(s[0])
step=0
while True:
    step+=1
    cnt=0
    fgrid=[[0]*w for i in range(h)]
    over9=[]
    for i in range(h):
        for j in range(w):
            o[i][j]+=1
            if o[i][j]>9:
                fgrid[i][j]=1
                over9.append((i,j))
    while len(over9):
        t,u=over9.pop()
        cnt+=1
        for dt,du in ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)):
            if 0<=t+dt<h and 0<=u+du<w:
                o[t+dt][u+du]+=1
                if o[t+dt][u+du]>9 and fgrid[t+dt][u+du]==0:
                    fgrid[t+dt][u+du]=1
                    over9.append((t+dt,u+du))
    for i in range(h):
        for j in range(w):
            if fgrid[i][j]:o[i][j]=0
    if cnt==h*w:
        print(step)
        break
