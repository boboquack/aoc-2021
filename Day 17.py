minx=288
maxx=330
miny=-96
maxy=-50
t=0
for vy in range(-96,96):
    k=vy
    for vx in range(331):
        x=0
        y=0
        while vx>0 or y>=miny:
            x+=vx
            y+=vy
            if minx<=x<=maxx and miny<=y<=maxy:
                t+=1
                break
            if vx>0:
                vx-=1
            vy-=1
        vy=k
print(t)
                
