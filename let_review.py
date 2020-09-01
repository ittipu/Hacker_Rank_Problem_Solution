n = int(input())
l = list()
inx = list()
for i in range(n):
    s = input()
    print(*["".join(s[::2]), "".join(s[1::2])])


