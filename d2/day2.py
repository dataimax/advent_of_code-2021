with open('day2input.txt') as f:
    input = [x for x in f]

#part 1
depth = 0
horiz = 0

for line in input:
    if line.startswith('forward'):
        horiz += int(line.split(' ')[1])
    elif line.startswith('down'):
        depth += int(line.split(' ')[1])
    elif line.startswith('up'):
        depth -= int(line.split(' ')[1])

final = depth*horiz
print(final)

#part 2
depth = 0
horiz = 0
aim = 0

for line in input:
    if line.startswith('forward'):
        horiz += int(line.split(' ')[1])
        depth += aim * int(line.split(' ')[1])
    elif line.startswith('down'):
        aim += int(line.split(' ')[1])
    elif line.startswith('up'):
        aim -= int(line.split(' ')[1])

final = depth*horiz
print(final)