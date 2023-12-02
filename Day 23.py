'''
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########

#print(4+40+200+5+6000+500+4+7000+30+40+700+3+8)

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########

print(4+40+300+3+6000+7000+30+40+800+3+8+500)

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########

print(200+10+4+40+6000+7000+500+30+40+700+3+3)

#############
#...........#
###B#A#B#C###
  #C#D#D#A#
  #########

print('min',40+700+5+7000+50+6000+600+9)

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########

print(200+5+9+8000+50+40+5000+500+700+3+3)

#############
#...........#
###B#A#B#C###
  #D#C#B#A#
  #D#B#A#C#
  #C#D#D#A#
  #########
'''

hall=[
    (0,0),
    (1,0),
    (3,0),
    (5,0),
    (7,0),
    (9,0),
    (10,0)
]
achim=[
    (2,1),
    (2,2),
    (2,3),
    (2,4)
]
bchim=[
    (4,1),
    (4,2),
    (4,3),
    (4,4)
]
cchim=[
    (6,1),
    (6,2),
    (6,3),
    (6,4)
]
dchim=[
    (8,1),
    (8,2),
    (8,3),
    (8,4)
]
chims=achim+bchim+cchim+dchim
loc={'A':2,'B':4,'C':6,'D':8}
clook={'A':1,'B':10,'C':100,'D':1000}
chim0=[2,4,6,8]
gchim={'A':achim,'B':bchim,'C':cchim,'D':dchim}

def clear(x,y,q,pos):
    if pos[y]!=None:return False
    if y[0] in chim0:
        if loc[q]!=y[0]:return False
        if any(pos[i]!=None and pos[i][0]!=q for i in gchim[q]):return False
    for i in hall:
        if min(x[0],y[0])<i[0]<max(x[0],y[0]) and pos[i]!=None:return False
    for i in chims:
        if i[0]==x[0] and i[1]<x[1] and pos[i]!=None:return False
        if i[0]==y[0] and i[1]<y[1] and pos[i]!=None:return False
    return True

def win(pos):
    if type(pos)==str:
        pos={eval(i):eval(j) for i,j in [k.split(':') for k in pos.split('\n')]}
    for i in pos:
        if pos[i]!=None and i[0]!=loc[pos[i][0]]:return False
    return True

cost=lambda x,y,q:(abs(x[0]-y[0])+abs(x[1]-y[1]))*clook[q]

spos={i:None for i in hall}|{j:(i,'s') for i,j in zip('BDDCACBDBBADCACA',chims)}
#spos={i:None for i in hall}|{j:(i,'s') for i,j in zip('BAAACDBBBCCCDADD',chims)}
#for x in chims:
#    if x[1]>=3:spos[x]=(spos[x][0],'f')

def pnice(pos):
    if type(pos)==str:
        pos={eval(i):eval(j) for i,j in [k.split(':') for k in pos.split('\n')]}
    out=''
    for i in range(11):
        if (i,0) in hall and pos[(i,0)]!=None:out+=pos[(i,0)][0]
        else:out+='.'
    for j in range(1,5):
        out+='\n'
        for i in range(11):
            if i not in chim0:out+=' '
            elif pos[(i,j)]!=None:
                if pos[(i,j)][1]=='s':
                    out+=pos[(i,j)][0]
                else:
                    out+=pos[(i,j)][0].lower()
            else:out+='.'
    print(out+'\n')

def tops(pos):
    top=[]
    for i in achim:
        if pos[i]!=None:
            if pos[i][1]=='s':
                top.append(i)
            break
    for i in bchim:
        if pos[i]!=None:
            if pos[i][1]=='s':
                top.append(i)
            break
    for i in cchim:
        if pos[i]!=None:
            if pos[i][1]=='s':
                top.append(i)
            break
    for i in dchim:
        if pos[i]!=None:
            if pos[i][1]=='s':
                top.append(i)
            break
    return top

halls=lambda pos:[i for i in hall if pos[i]!=None]

spots=hall+chims

spos='\n'.join(str(i)+':'+str(spos[i]) for i in spots)

import heapq
pq=[(0,spos)]
count=0
seen={}
while not win(pq[0][1]):
    count+=1
    c,pos=heapq.heappop(pq)
    if pos in seen and seen[pos]<c:continue
    pos={eval(i):eval(j) for i,j in [k.split(':') for k in pos.split('\n')]}
    #if c==3510 and sum(pos[i]!=None for i in hall)==1:# and pos[(3,0)]!=None and pos[(3,0)][0]=='B':
    #    pnice(pos)
    #    break
    #while len(pq) and pq[0]==(c,pos):heapq.heappop(pq)
    if count%1000==0:print(count,c,len(pq))
    for x in halls(pos):
        q=pos[x][0]
        if not any(pos[i]!=None and pos[i][0]!=q for i in gchim[q]):
            for y in gchim[q][::-1]:
                if pos[y]==None:
                    if clear(x,y,q,pos):
                        newpos={i:pos[i] for i in pos}
                        newc=c+cost(x,y,q)
                        newpos[y]=(q,'f')
                        newpos[x]=None
                        newpos='\n'.join(str(i)+':'+str(newpos[i]) for i in spots)
                        if newpos not in seen or newc<seen[newpos]:
                            heapq.heappush(pq,(newc,newpos))
                            seen[newpos]=newc
                    break
    for x in tops(pos):
        q=pos[x][0]
        for y in hall:
            if clear(x,y,q,pos):
                newpos={i:pos[i] for i in pos}
                newc=c+cost(x,y,q)
                newpos[y]=(q,'m')
                newpos[x]=None
                newpos='\n'.join(str(i)+':'+str(newpos[i]) for i in spots)
                if newpos not in seen or newc<seen[newpos]:
                    heapq.heappush(pq,(newc,newpos))
                    seen[newpos]=newc
    #break
    
print(pq[0][0])
