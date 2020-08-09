set_A_len = int(input())
set_A = set(int(x) for x in input().split())
set_B_len = int(input())
set_B = set(int(x) for x in input().split())

new_set = set_A.symmetric_difference(set_B)

sort_set = sorted(new_set)
for i in sort_set:
    print(i)
