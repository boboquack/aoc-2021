instrs=['''inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y''',
'''inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y''',
'''inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y''',
'''inp w
mul x 0
add x z
mod x 26
div z 26
add x -14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y''',
'''inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y''',
'''inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y''',
'''inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 14
mul y x
add z y''',
'''inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y''',
'''inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y''',
'''inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y''',
'''inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y''',
'''inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y''',
'''inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y''',
'''inp w
mul x 0
add x z
mod x 26
div z 26
add x -10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y''']

def run(prog,ins,z=0):
    prog=[i.split() for i in prog.split('\n')]
    ins=list(str(ins))
    d={'w':0,'x':0,'y':0,'z':z}
    for t in prog:
        if t==['eql','x','w'] and ['div','z','26'] in prog and d['x']!=d['w']:            return None
        if t[0]=='inp':
            d[t[1]]=int(ins.pop(0))
        else:
            a=d[t[1]]
            if t[2] in 'wxyz':
                b=d[t[2]]
            else:
                b=int(t[2])
            if t[0]=='add':
                d[t[1]]+=b
            elif t[0]=='mul':
                d[t[1]]*=b
            elif t[0]=='div':
                if b==0:raise ZeroDivisionError
                if b>0:
                    if a>=0:
                        d[t[1]]=a//b
                    else:
                        d[t[1]]=-((-a)//b)
                if b<0:
                    if a<=0:
                        d[t[1]]=(-a)//(-b)
                    else:
                        d[t[1]]=-(a//(-b))
            elif t[0]=='mod':
                if b<=0 or a<0:raise ZeroDivisionError
                d[t[1]]=a%b
            elif t[0]=='eql':
                d[t[1]]=int(a==b)
            else:raise SyntaxError
    return d['z']
prog='\n'.join(instrs)
zs={0:0}
for i in range(14):
    newzs={}
    for z in zs:
        for k in range(1,10):
            m=zs[z]*10+k
            oz=run(instrs[i],k,z)
            if oz==None:continue
            if oz in newzs:
                newzs[oz]=max(newzs[oz],m)
            else:
                newzs[oz]=m
    zs=newzs
    print(i+1,'/ 14 complete: ',len(zs))
print(zs[0])
zs={0:0}
for i in range(14):
    newzs={}
    for z in zs:
        for k in range(1,10):
            m=zs[z]*10+k
            oz=run(instrs[i],k,z)
            if oz==None:continue
            if oz in newzs:
                newzs[oz]=min(newzs[oz],m)
            else:
                newzs[oz]=m
    zs=newzs
    print(i+1,'/ 14 complete: ',len(zs))
print(zs[0])
