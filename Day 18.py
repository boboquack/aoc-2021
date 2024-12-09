s=INPUT.split()
t=s[:]
if any(i not in '0123456789,[]' for j in s for i in j):raise Exception
s=[eval(i) for i in s]
t=[eval(i) for i in t]

def depth(n):
    if type(n)==int:return n
    a,b=n
    return 1+max(depth(a),depth(b))

def incrr(n,k):
    if type(n)==int:return n+k
    a,b=n
    return [a,incrr(b,k)]

def incrl(n,k):
    if type(n)==int:return n+k
    a,b=n
    return [incrl(a,k),b]

def expl(n,d):
    if type(n)==int:return (n,False,0,0)
    a,b=n
    if d<4:
        a,x,l,r=expl(a,d+1)
        if x:
            if r:
                b=incrl(b,r)
            return ([a,b],True,l,0)
        b,x,l,r=expl(b,d+1)
        if l:
            a=incrr(a,l)
        return ([a,b],x,0,r)
    return (0,True,a,b)

def split(n):
    if type(n)==int:
        if n>=10:
            return ([n//2,(n+1)//2],True)
        return (n,False)
    a,b=n
    a,x=split(a)
    if x:
        return ([a,b],True)
    b,x=split(b)
    return ([a,b],x)

def norm(n):
    while True:
        n,b,l,r=expl(n,0)
        if not b:
           n,b=split(n)
           if not b:
               return n

def mag(n):
    if type(n)==int:return n
    a,b=n
    return 3*mag(a)+2*mag(b)

def add(a,b):
    return norm([a,b])

while len(s)>=2:
    q=s.pop(0)
    s[0]=add(q,s[0])
print(mag(s[0]))

u=0
for i in t:
    for j in t:
        if i!=j:
            u=max(u,mag(add(i,j)))
print(u)
