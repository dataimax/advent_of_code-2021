with open('day8.txt') as f:
    input = [tuple(x.replace('\n','').split(' | ')) for x in f]

count= 0
for row in input:
    for code in row[1].split():
        if len(code) in [2,3,4,7]:
            count+=1
print("PART 1: ", count)

def intersect(s1,s2):
    res = ""
    for i in s1:
        if i in s2 and not i in res:
            res += i
    return set(''.join(sorted(res)))

def get_digits(crack,output):
    output_s = [''.join(sorted(ele)) for ele in output.split()]
    res=""
    for dig in output_s:
        #print(dig)
        res+=crack[dig]
    return res

def crack_code(row):
    digits = [''.join(sorted(ele)) for ele in row.split()]
    known_1 = set([x for x in digits if len(x) == 2][0])
    known_4 = set([x for x in digits if len(x) == 4][0])
    known_7 = set([x for x in digits if len(x) == 3][0])
    known_8 = set([x for x in digits if len(x) == 7][0])

    unknown_len5 = [set(x) for x in digits if len(x) == 5]
    unknown_len6 = [set(x) for x in digits if len(x) == 6]
    intersect_5s = unknown_len5[0].intersection(unknown_len5[1]).intersection(unknown_len5[2])
    intersect_6s = unknown_len6[0].intersection(unknown_len6[1]).intersection(unknown_len6[2])
    s_top = known_7.intersection(intersect_5s)
    s_mid = intersect_5s.intersection(intersect(known_8,known_4))
    
    known_0 = known_8-s_mid
    known_5 = intersect_6s.union(s_mid)
    s_bot = known_5-known_4-s_top
    known_3 = known_7.union(s_mid).union(s_bot)
    known_9 = known_3.union(known_5)
    s_bleft = known_8-known_9
    
    known_6 = known_5.union(s_bleft)
    s_tright = known_8-known_6
    known_2 = intersect_5s.union(s_tright).union(s_bleft)
    return {''.join(sorted(known_0)):'0', ''.join(sorted(known_1)):'1',''.join(sorted(known_2)):'2',''.join(sorted(known_3)):'3',''.join(sorted(known_4)):'4',''.join(sorted(known_5)):'5',''.join(sorted(known_6)):'6',''.join(sorted(known_7)):'7', ''.join(sorted(known_8)):'8',''.join(sorted(known_9)):'9'}

sum= 0
for row in input:
    crack = crack_code(row[0])
    sum+=int(get_digits(crack,row[1]))

print("PART2:",sum)