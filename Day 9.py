s=INPUT.split('\n')
s=[[int(i) for i in j] for j in s]
h=len(s)
w=len(s[0])
tot=0
for r in range(h):
    for c in range(w):
        for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
            if 0<=r+dr<h and 0<=c+dc<w and s[r+dr][c+dc]<=s[r][c]:
                 break
        else:
            tot+=s[r][c]+1
print(tot)     

bcount=-1
bas=[[None]*w for i in range(h)]
for r in range(h):
    for c in range(w):
        if bas[r][c]==None and s[r][c]<9:
            bcount+=1
            stack=[(r,c)]
            while stack!=[]:
                r,c=stack.pop()
                bas[r][c]=bcount
                for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                    if 0<=r+dr<h and 0<=c+dc<w and bas[r+dr][c+dc]==None and s[r+dr][c+dc]!=9:
                        stack.append((r+dr,c+dc))
t=[0]*(bcount+1)
for r in range(h):
    for c in range(w):
        if bas[r][c]:
            t[bas[r][c]]+=1
t.sort()
print(t[-1]*t[-2]*t[-3])
