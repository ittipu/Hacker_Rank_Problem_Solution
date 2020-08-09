m, n = [int(x) for x in input().split()]
array = [int(x) for x in input().split()]
A = set(int(x) for x in input().split())
B = set(int(x) for x in input().split())
happiness = 0

for i in array:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1
print(happiness)

