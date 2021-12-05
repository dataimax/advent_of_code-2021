with open('day5.txt') as f:
    data_raw = [x.replace('\n','') for x in f]

coords=[]
for data in data_raw:
    coords.append([x.split(',') for x in data.split(' -> ')])

import numpy as np
diagramp1 = np.zeros(shape=(1000,1000))
diagramp2 = np.zeros(shape=(1000,1000))


def high_and_low(c1,c2):
    if c1<c2:
        return c1,c2
    else:
        return c2,c1

### Part 1 ###
lin_and_vert = [x for x in coords if (int(x[0][0])==int(x[1][0]) or int(x[0][1])==int(x[1][1]))]
    #data = [x for x in f if ()]


def p1():
    for coords in lin_and_vert:
        x1,x2,y1,y2 = int(coords[0][0]),int(coords[1][0]),int(coords[0][1]),int(coords[1][1])
        if x1==x2:
            l,h = high_and_low(y1,y2)
            while(l<=h):
                diagramp1[x1][l] +=1
                l+=1
        else:
            l,h = high_and_low(x1,x2)
            while(l<=h):
                diagramp1[l][y1] +=1
                l+=1

###Part 2###
def direction(x1,x2,y1,y2):
    if x1<x2 and y1<y2:
        return 1
    elif x1>x2 and y1>y2:
        return 2
    elif x1<x2 and y1>y2:
        return 3
    elif x1>x2 and y1<y2:
        return 4
    
def p2():
    for coord in coords:
        x1,x2,y1,y2 = int(coord[0][0]),int(coord[1][0]),int(coord[0][1]),int(coord[1][1])
        if x1==x2:
            l,h = high_and_low(y1,y2)
            while(l<=h):
                diagramp2[x1][l] +=1
                l+=1

        elif y1==y2:
            l,h = high_and_low(x1,x2)
            while(l<=h):
                diagramp2[l][y1] +=1
                l+=1
        
        else:
            if direction(x1,x2,y1,y2) == 1:
                while(x1<=x2):
                    diagramp2[x1][y1] +=1
                    x1+=1
                    y1+=1
            elif direction(x1,x2,y1,y2) == 2:
                while(x1>=x2):
                    diagramp2[x1][y1] +=1
                    x1-=1
                    y1-=1
            elif direction(x1,x2,y1,y2) == 3:
                while(x1<=x2):
                    diagramp2[x1][y1] +=1
                    x1+=1
                    y1-=1
            else:
                while(y1<=y2):
                    diagramp2[x1][y1] +=1
                    x1-=1
                    y1+=1
p1()
p2()
print(diagramp1[diagramp1>=2].size)
print(diagramp2[diagramp2>=2].size)