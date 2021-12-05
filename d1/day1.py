with open('input.txt') as f:
    input = [int(x) for x in f]

#Part 1
count = 0
prew = input[1]

for i in input:
    if prew < i:
        count+=1
    prew=i

print(count)
#Part 2
count=0
for j in range(1,len(input)-2):
    k=j+1
    first = input[j-1]+input[j]+input[j+1]
    snd = input[k-1]+input[k]+input[k+1]

    if snd > first:
        count+=1

print(count)