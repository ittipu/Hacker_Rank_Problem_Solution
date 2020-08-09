num = int(input())
hotel = [int(x) for x in input().split()]
set_A = set()
set_B = set()
for i in hotel:
    if i in set_A:
        set_B.add(i)
    else:
        set_A.add(i)
captain_room = set_A.difference(set_B)

print(captain_room.pop())
