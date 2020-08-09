test_case = int(input())
for i in range(test_case):
    len_A = int(input())
    set_A = set(int(x) for x in input().split())
    len_B = int(input())
    set_B = set(int(x) for x in input().split())
    if set_A.issubset(set_B):
        print("True")
    else:
        print("False")
