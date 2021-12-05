with open('day3input.txt') as f:
    input = [x.replace('\n', '') for x in f]


gamma = []
epsilon = []
co2, o2 = input[:],input[:]
verticals = [[y[x] for y in input] for x in range(len(input[0]))]
print(o2[0][0])
for j,x in enumerate(verticals):
    most = 0 if x.count('0')>x.count('1') else 1
    print(most)
    gamma.append(most)
    epsilon.append(int(not(most)))
    if len(o2)>1:
        o2_verticals = [[y[x] for y in o2] for x in range(len(o2[0]))]
        common = 0 if x.count('0')>x.count('1') else 1
        o2 = [y for y in o2 if int(y[j]) == (0 if o2_verticals[j].count('0')>o2_verticals[j].count('1') else 1)]
        
    if len(co2)>1:
        co2_verticals = [[y[x] for y in co2] for x in range(len(co2[0]))]
        co2 = [y for y in co2 if int(y[j]) != (0 if co2_verticals[j].count('0')>co2_verticals[j].count('1') else 1)]
    
    print("len :", len(o2))
    print("len :", len(co2))

print(int(co2[0],2), int(o2[0],2))
print(int(co2[0],2)*int(o2[0],2))
print(int(''.join([str(x) for x in gamma]), 2) * int(''.join([str(x) for x in epsilon]), 2))
