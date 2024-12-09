s=INPUT.split('\n')
t=[[[0]*101 for i in range(101)] for i in range(101)]
u=[]
for i in s:
    j,k=i.split()
    x,y,z=k.split(',')
    a,xa=x.split('=')
    b,yb=y.split('=')
    c,zc=z.split('=')
    x1,x2=map(int,xa.split('..'))
    y1,y2=map(int,yb.split('..'))
    z1,z2=map(int,zc.split('..'))
    u.append((j=='on',x1,x2+1,y1,y2+1,z1,z2+1))
    if not(50<x1 or 50<y1 or 50<z1 or -50>x2 or -50>y2 or -50>z2):
        for x in range(x1,x2+1):
            if -50<=x<=50:
                for y in range(y1,y2+1):
                    if -50<=y<=50:
                        for z in range(z1,z2+1):
                            if -50<=z<=50:
                                if j=='on':
                                    t[x][y][z]=1
                                else:
                                    t[x][y][z]=0
print(sum(sum(sum(i) for i in j) for j in t))

tot=0
xs=sorted(set(i[1] for i in u)|set(i[2] for i in u))
q=0
for lx,rx in zip(xs,xs[1:]):
    q+=1
    #if q%10==0:print('Working on',q,'out of',len(xs)-1)
    ys=sorted(set(i[3] for i in u if not(i[1]>=rx or i[2]<=lx))|set(i[4] for i in u if not(i[1]>=rx or i[2]<=lx)))
    for ly,ry in zip(ys,ys[1:]):
        zs=sorted(set(i[5] for i in u if not(i[1]>=rx or i[2]<=lx or i[3]>=ry or i[4]<=ly))|set(i[6] for i in u if not(i[1]>=rx or i[2]<=lx or i[3]>=ry or i[4]<=ly)))
        for lz,rz in zip(zs,zs[1:]):
            state=0
            for on,x1,x2,y1,y2,z1,z2 in u:
                if x1<=lx and rx<=x2 and y1<=ly and ry<=y2 and z1<=lz and rz<=z2:
                    if on:
                        state|=1
                    else:
                        state&=0
            #print(state,rz,lz,ry,ly,rx,lx)
            tot+=state*(rz-lz)*(ry-ly)*(rx-lx)
print(tot)
