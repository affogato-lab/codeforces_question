import sys
lines = sys.stdin.readlines()
n_cases = int(lines[0].strip())

for i in range(1, len(lines), 2):
    j = i+1
    answer = 'NO'
    n_gears = int(lines[i].strip())
    gears = lines[j].split()
    gears_dict = {x:0 for x in gears}
    for x in gears:
        gears_dict[x]+=1
        if gears_dict[x]>1: 
            answer = 'YES'
            break
    print(answer)