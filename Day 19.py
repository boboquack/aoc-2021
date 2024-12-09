data=INPUT.split('\n\n')

"""
data=SAMPLE.split('\n\n')
"""

scanners=[[tuple(int(k) for k in j.split(',')) for j in i.split('\n')[1:]] for i in data]
scanners={i:scanners[i] for i in range(len(scanners))}

import itertools
sdist=lambda z1,z2:tuple(sorted(abs(i-j) for i,j in zip(z1,z2)))

def fmatch(a1,a2,c1,c2,xflip,yflip,zflip,xyzmap):
    #print(xflip,yflip,zflip,[xyzmap(i) for i in range(3)])
    b1=[c1[xyzmap(i)] for i in range(3)]
    b2=[c2[xyzmap(i)] for i in range(3)]
    if xflip and a1[0]-a2[0]!=xflip*(b1[0]-b2[0]):
        return [False,0,0,0]
    elif xflip==0 and abs(a1[0]-a2[0])!=abs(b1[0]-b2[0]):
        return [False,0,0,0]
    if xflip==0 and abs(a1[0]-a2[0])!=0:
        xflip=(a1[0]-a2[0])//(b1[0]-b2[0])
    if yflip and a1[1]-a2[1]!=yflip*(b1[1]-b2[1]):
        return [False,0,0,0]
    elif yflip==0 and abs(a1[1]-a2[1])!=abs(b1[1]-b2[1]):
        return [False,0,0,0]
    if yflip==0 and abs(a1[1]-a2[1])!=0:
        yflip=(a1[1]-a2[1])//(b1[1]-b2[1])
    if zflip and a1[2]-a2[2]!=zflip*(b1[2]-b2[2]):
        return [False,0,0,0]
    elif zflip==0 and abs(a1[2]-a2[2])!=abs(b1[2]-b2[2]):
        return [False,0,0,0]
    if zflip==0 and abs(a1[2]-a2[2])!=0:
        zflip=(a1[2]-a2[2])//(b1[2]-b2[2])
    return [True,xflip,yflip,zflip]

def getthis(vdist,tup,hmm):
    v=[]
    u=[0]*12
    for a1 in hmm[tup[0]]:
        u[0]=a1
        for a2 in hmm[tup[1]]:
            u[1]=a2
            if all(vdist[tup[1]][tup[i]]==sdist(u[1],u[i]) for i in range(1)):
                for a3 in hmm[tup[2]]:
                    u[2]=a3
                    if all(vdist[tup[2]][tup[i]]==sdist(u[2],u[i]) for i in range(2)):
                        for a4 in hmm[tup[3]]:
                            u[3]=a4
                            if all(vdist[tup[3]][tup[i]]==sdist(u[3],u[i]) for i in range(3)):
                                for a5 in hmm[tup[4]]:
                                    u[4]=a5
                                    if all(vdist[tup[4]][tup[i]]==sdist(u[4],u[i]) for i in range(4)):
                                        for a6 in hmm[tup[5]]:
                                            u[5]=a6
                                            if all(vdist[tup[5]][tup[i]]==sdist(u[5],u[i]) for i in range(5)):
                                                for a7 in hmm[tup[6]]:
                                                    u[6]=a7
                                                    if all(vdist[tup[6]][tup[i]]==sdist(u[6],u[i]) for i in range(6)):
                                                        for a8 in hmm[tup[7]]:
                                                            u[7]=a8
                                                            if all(vdist[tup[7]][tup[i]]==sdist(u[7],u[i]) for i in range(7)):
                                                                for a9 in hmm[tup[8]]:
                                                                    u[8]=a9
                                                                    if all(vdist[tup[8]][tup[i]]==sdist(u[8],u[i]) for i in range(8)):
                                                                        for a10 in hmm[tup[9]]:
                                                                            u[9]=a10
                                                                            if all(vdist[tup[9]][tup[i]]==sdist(u[9],u[i]) for i in range(9)):
                                                                                for a11 in hmm[tup[10]]:
                                                                                    u[10]=a11
                                                                                    if all(vdist[tup[10]][tup[i]]==sdist(u[10],u[i]) for i in range(10)):
                                                                                        for a12 in hmm[tup[11]]:
                                                                                            u[11]=a12
                                                                                            if all(vdist[tup[11]][tup[i]]==sdist(u[11],u[i]) for i in range(11)):
                                                                                                v.append(tuple(u))
    return v                   

a=lambda j:[0,1,2][j]
b=lambda j:[0,2,1][j]
c=lambda j:[1,0,2][j]
d=lambda j:[1,2,0][j]
e=lambda j:[2,0,1][j]
f=lambda j:[2,1,0][j]
mapcol=[a,b,c,d,e,f]

scanloc={0:(0,0,0)}
beacons=[i for i in scanners[0]]
del scanners[0]
while len(scanners):
    sdists={sdist(i,j) for i in beacons for j in beacons if i!=j}
    try:
        for scanind in scanners:
            scanner=scanners[scanind]
            vdist=[[(0,0,0)]*len(scanner) for i in range(len(scanner))]
            for i in range(len(scanner)):
                for j in range(len(scanner)):
                    if sdist(scanner[i],scanner[j]) in sdists:
                        vdist[i][j]=sdist(scanner[i],scanner[j])
            r=[i for i in range(len(scanner)) if sum(j!=(0,0,0) for j in vdist[i])>=11]
            if len(r)>=12:
                for tup in itertools.combinations(r,12):
                    if all((j==k or vdist[j][k]!=(0,0,0)) for j in tup for k in tup):
                        hmm={k:[] for k in tup}
                        for i in beacons:
                            l={sdist(i,j) for j in beacons}
                            for k in tup:
                                if all(vdist[k][u] in l for u in tup):
                                    hmm[k].append(i)
                        ahh=getthis(vdist,tup,hmm)
                        #print(scanind,[scanner[k] for k in tup],ahh,hmm)
                        for v in ahh:
                            for xyzmap in mapcol:
                                bloop={tup[k]:v[k] for k in range(12)}
                                xflip=0
                                yflip=0
                                zflip=0
                                kk=tup[0]
                                for k in tup[1:]:
                                    b,xflip,yflip,zflip=fmatch(bloop[kk],bloop[k],scanner[kk],scanner[k],xflip,yflip,zflip,xyzmap)
                                    if not b:
                                        break
                                else:
                                    scanx=bloop[kk][0]-scanner[kk][xyzmap(0)]*xflip
                                    scany=bloop[kk][1]-scanner[kk][xyzmap(1)]*yflip
                                    scanz=bloop[kk][2]-scanner[kk][xyzmap(2)]*zflip
                                    scanloc[scanind]=(scanx,scany,scanz)
                                    beacons=set(beacons)
                                    for beacon in scanner:
                                        beacx=scanx+beacon[xyzmap(0)]*xflip
                                        beacy=scany+beacon[xyzmap(1)]*yflip
                                        beacz=scanz+beacon[xyzmap(2)]*zflip
                                        beacons.add((beacx,beacy,beacz))
                                    beacons=list(beacons)
                                    #print('Found',scanind,'at',scanloc[scanind],'|',len(beacons),'beacons')
                                    del scanners[scanind]
                                    raise IOError
        else:
            #print('Not found')
            raise ZeroDivisionError
    except IOError:
        pass
print(len(beacons))    

mdist=lambda x,y:sum(abs(i-j) for i,j in zip(x,y))
print(max(mdist(scanloc[x],scanloc[y]) for x in scanloc for y in scanloc))
