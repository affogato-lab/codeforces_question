# Redstone?

# 结果：
- Python 3: 运行时间109ms，存储3300KB

## 问题描述
> Steve stumbled upon a collection of $n$ gears, where gear $i$ has $a_{i}$ teeth, and he wants to arrange them into a row. After he arranges them, Steve will spin the leftmost gear at a speed of 1 revolution per second. For each of the other gears, let $x$ be the number of teeth it has, $y$ be the number of teeth of the gear to its left, and $z$ be the speed the gear to its left spins at. Then, its speed will be $\frac{y}{x}z$ revolutions per second. Steve considers the contraption satisfactory if the rightmost gear spins at a speed of 1 revolution per second. Determine whether Steve can rearrange the gears into a satisfactory contraption.

## 思路：
1. Base case: 假设只有两个齿轮，则
   $$
   z_1 = \frac{z_0}{z_1}
   $$
2. Inductive step: 不难发现
   $$
   z_n = \frac{x_{n-1}}{x_n}\cdot \frac{x_{n-2}}{x_{n-1}}\cdot\dots\cdot \frac{x_0}{x_1} = \frac{x_0}{x_n}
   $$
   因此，如果$z_n = 1$，则$x_0 = x_n$。也就是说，只要满足a中有至少两个相同的数，则满足题中条件。

## 代码
```Python 
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
``` 