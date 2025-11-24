# Number Maze

## 结果
Python 3: 运行时间93ms，存储2800KB

## 问题描述
详情见[Number Maze 原题](https://codeforces.com/contest/2172/problem/E)
大致意思：

对于给定的$n\in \{12, 123, 1234\}$，考虑n的所有数字排列，并将这些排列按升序排序。找出排序后的第$j$个和第$k$个排列中位置相同，数字也相同的个数（记为x）和数字相同，位置不同的个数（记为y）

## 思路
1. 首先是要找出n的所有排列组合方式，并按升序排列。`itertools`中有现成的实现方法
2. 因为两个排列是均为同一字符串中元素的排列组合，它们的元素也相同。也就是说如果同一位置上元素不同，那么一定在其他位置上有对应元素。举个例子：3421和4321都是1234的排列组合，第一位上数字不同但均在其他位置出现。
3. 所以对每个字符串n，遍历一遍，找出有多少`perm_j[i]==perm_k[i]`，得到x；最后用n的长度减去x，得到y即可

## 代码
```{python}
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
```