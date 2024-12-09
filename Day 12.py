s=INPUT.split()
d={}
for i in s:
    j,k=i.split('-')
    if j in d:
        d[j].append(k)
    else:
        d[j]=[k]
    if k in d:
        d[k].append(j)
    else:
        d[k]=[j]

vis={i:False for i in d if i==i.lower()}
cnt=0
def trav(loc,vis):
    global cnt
    if loc=='end':
        cnt+=1
        return
    if loc==loc.lower():
        vis={i:vis[i] for i in vis}
        vis[loc]=1
    for i in d[loc]:
        if i!=i.lower() or vis[i]==0:
            trav(i,vis)
trav('start',vis)
print(cnt)
vis={i:0 for i in d if i==i.lower()}
vis['start']=2
cnt=0
blue=0
def trav2(loc,vis,path):
    global cnt,blue
    blue+=1
    path=path[:]+[loc]
    #if blue%10000==0:print(blue,loc,vis,path)
    if loc=='end':
        cnt+=1
        return
    if loc==loc.lower():
        vis={i:vis[i] for i in vis}
        vis[loc]+=1
    for i in d[loc]:
        if i!=i.lower() or vis[i]==0 or (vis[i]==1 and all(vis[i]<2 for i in vis if i!='start')):
            trav2(i,vis,path)
trav2('start',vis,[])
print(cnt)
    
    
