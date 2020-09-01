n = int(input())
for i in range(n):
    try:
        a, b = [int(x) for x in input().split()]
        print(a//b)
    except BaseException as e:
        print("Error Code:", e)

