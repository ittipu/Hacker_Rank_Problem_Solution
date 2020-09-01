from collections import defaultdict

a, b = [int(x) for x in input().split()]

alist = list()
for ch in range(a):
    alist.append(input())

blist = list()
for l in range(b):
    blist.append(input())


d = defaultdict(list)

for i in range(a):
    d[alist[i]].append(i+1)


for i in blist:
    if i in d:
        print(*d[i])
    else:
        print(-1)