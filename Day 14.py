s='OFSVVSFOCBNONHKFHNPK'
t='''HN -> C
VB -> K
PF -> C
BO -> F
PB -> F
OH -> H
OB -> N
PN -> O
KO -> V
CK -> V
FP -> H
PC -> V
PP -> N
FN -> N
CC -> F
FC -> N
BP -> N
SH -> F
NS -> V
KK -> B
HS -> C
NV -> N
FO -> B
VO -> S
KN -> F
SC -> V
NB -> H
CH -> B
SF -> V
NP -> V
FB -> P
CV -> B
PO -> P
SV -> P
OO -> V
PS -> C
CO -> N
SP -> B
KP -> H
KH -> S
KS -> S
NH -> K
SS -> P
PV -> P
KV -> V
ON -> N
BS -> C
HP -> K
SB -> P
VC -> B
HB -> N
FS -> V
VP -> K
BB -> N
FK -> S
CS -> P
SO -> F
HF -> F
VV -> C
BC -> S
SN -> K
KB -> H
BN -> H
HO -> S
KC -> F
CP -> S
HC -> S
OS -> K
NK -> N
BF -> S
VN -> B
SK -> K
HV -> B
KF -> H
FV -> B
VF -> H
BH -> S
NN -> O
HH -> K
CN -> H
PH -> V
NF -> S
OV -> P
OC -> V
OK -> H
OF -> H
HK -> N
FH -> P
BK -> N
VS -> H
NO -> V
VK -> K
CF -> N
CB -> N
NC -> K
PK -> B
VH -> F
FF -> C
BV -> P
OP -> K'''.split('\n')
t=[j.split(' -> ') for j in t]
u={i:j for i,j in t}
for i in range(10):
    v=''
    for i in range(len(s)-1):
        j,k=s[i],s[i+1]
        if j+k in u:
            v+=u[j+k]
        else:
            v+=' '
    w=s[0]
    for i in range(len(s)-1):
        w+=v[i]
        w+=s[i+1]
    s=w
t=[s.count(i) for i in set(s)]
t.sort()
print(t[-1]-t[0])
s='OFSVVSFOCBNONHKFHNPK'
d={}
for i in range(len(s)-1):
    if s[i:i+2] in d:
        d[s[i:i+2]]+=1
    else:
        d[s[i:i+2]]=1
for i in range(40):
    e={}
    for i in d:
        if i in u:
            p=i[0]+u[i]
            q=u[i]+i[1]
            if p in e:
                e[p]+=d[i]
            else:
                e[p]=d[i]
            if q in e:
                e[q]+=d[i]
            else:
                e[q]=d[i]
        else:
            if i in e:
                e[i]+=d[i]
            else:
                e[i]=d[i]
    d=e
v={s[-1]:1,s[0]:1}
for i in d:
    for j in i:
        if j in v:
            v[j]+=d[i]
        else:
            v[j]=d[i]
print((max(v.values())-min(v.values()))//2)
            
