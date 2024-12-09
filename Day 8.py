s=INPUT.split('\n')
u=[[i.split() for i in j.split(' | ')] for j in s]
t=0
for i in u:
        for k in i[1]:
                t+=(1 if len(k) in [2,3,4,7] else 0)
print(t)
t=0
for i in u:
    for j in i[0]:
        if len(j)==2:
            one=set(j)
        if len(j)==3:
            seven=set(j)
        if len(j)==4:
            four=set(j)
        if len(j)==7:
            eight=set(j)
    for j in i[0]:
        if len(j)==6 and len(set(j)|four)==6:
            nine=set(j)
    for j in i[0]:
        if len(j)==5 and len(set(j)|nine)!=6:
            two=set(j)
    for j in i[0]:
        if len(j)==5 and len(set(j)^two)==2:
            three=set(j)
        if len(j)==5 and len(set(j)^two)==4:
            five=set(j)
    for j in i[0]:
        if len(j)==6 and len(set(j)|five)==6 and set(j)!=nine:
            six=set(j)
        if len(j)==6 and len(set(j)|five)==7:
            zero=set(j)
    d={0:zero,1:one,2:two,3:three,4:four,5:five,6:six,7:seven,8:eight,9:nine}
    p=0
    for j in i[1]:
        for k in d:
            if d[k]==set(j):
                p*=10
                p+=k
    t+=p
print(t)
