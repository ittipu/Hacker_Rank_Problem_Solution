val = int(input())
set_N = set(int(x) for x in input().split())
commands = int(input())

for i in range(commands):
    command = [str(x) for x in input().split()]
    new_set = set(int(x) for x in input().split())
    if command[0] == "intersection_update":
        set_N.intersection_update(new_set)

    elif command[0] == "update":
        set_N.update(new_set)

    elif command[0] == "symmetric_difference_update":
        set_N.symmetric_difference_update(new_set)

    elif command[0] == "difference_update":
        set_N.difference_update(new_set)

sum_of_set = 0
for value in set_N:
    sum_of_set = sum_of_set + value
print(sum_of_set)
