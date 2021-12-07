import statistics
import math
from collections import Counter
with open('day7.txt') as f:
    data = f.readline().replace('\n','').split(',')


def closest_to_med(med, tuples):
    current_min = 0
    current_diff = med
    for x in tuples:
        if abs(med-x[0])< current_diff:
            current_min = x[0]
            current_diff = med-x[0]

    return current_min
def fuel_cost(steps):
    cost = 0
    for i in range(1,steps+1):
        cost += i
    return cost
#PART 1
data = list(map(int, data))
med = statistics.median(data)
count = Counter(data)
x = count.most_common()
pos1 = closest_to_med(med,x)
fuel = 0
for num in data:
    fuel += int(abs(num-pos1))

print("PART 1: ", fuel)

#PART 2
avg = math.floor(statistics.mean(data))
fuel = sum(sum(range(abs(x - avg)+1)) for x in data)

print("PART 2:" ,fuel)