import sys
from itertools import permutations

lines = sys.stdin.readlines()
n_cases = int(lines[0].strip())

for i in range(1, len(lines)):
    l = lines[i].rstrip().split()
    perms = [''.join(p) for p in permutations(l[0])]
    left = perms[int(l[1])-1]
    right = perms[int(l[2])-1]
    x = 0
    total_len = len(left)
    y = 0
    for i in range(total_len):
        if left[i]==right[i]: x+=1
    y = total_len-x
    print(f'{x}A{y}B')
