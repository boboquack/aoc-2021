s=INPUT1.split()
coords=[i.split(',') for i in s]
coords=[[int(i),int(j)] for i,j in coords]

instrs=INPUT2.split()[2::3]
instrs=[i.split('=') for i in instrs]
instrs=[[i,int(j)] for i,j in instrs]

n=2000
k=[[0]*n for i in range(n)]
for x,y in coords:
    k[x][y]=1

for d,v in instrs:
    if d=='x':
        r=k[v+1:]
        for i in range(v):
            for j in range(len(k[0])):
                if k[i][j]:r[v-i-1][j]|=1
        k=r
    if d=='y':
        r=[i[v+1:] for i in k]
        for i in range(v):
            for j in range(len(k)):
                if k[j][i]:r[j][v-i-1]|=1
        k=r
    if [d,v]==instrs[0]:print(sum(sum(i) for i in k))
for i in list(zip(*k[::-1]))[::-1]:
    if sum(i)!=0:
        print(''.join('#' if j else ' ' for j in i).strip())
