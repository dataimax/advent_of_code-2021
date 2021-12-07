import numpy as np
from functools import lru_cache
with open('day6.txt') as f:
    input = f.readline().replace('\n','').split(',')

data = np.asfarray(input)
@lru_cache
def create_fish(start,days_left):
    days_left-=(start+1)
    if days_left<0:
        return 1
    
    count= create_fish(8,days_left)
    while days_left>=7:
        days_left -= 7
        count+= create_fish(8,days_left)
    
    return 1 + count

print("Part 1:", sum(create_fish(x, 80) for x in data))
print("Part 2:", sum(create_fish(x, 256) for x in data))
