set_A = set([int(x) for x in input().split()])
set_list = []
for i in range(int(input())):
    set_list.append(set_A.issuperset(set([int(x) for x in input().split()])))
print(all(set_list))


