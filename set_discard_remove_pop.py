n = int(input())
set_N = set(int(x) for x in input().split())
commands = int(input())
for i in range(commands):
    command = [str(x) for x in input().split()]
    if command[0] == "pop":
        set_N.pop()
    elif command[0] == "discard":
        set_N.discard(int(command[1]))
    elif command[0] == "remove":
        set_N.remove(int(command[1]))
sum_of_set = 0
for value in set_N:
    sum_of_set = sum_of_set + value
print(sum_of_set)
