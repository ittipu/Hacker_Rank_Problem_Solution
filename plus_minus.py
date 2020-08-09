num = int(input())
value_array = [int(x) for x in input().split()]
positive = 0
negative = 0
zero = 0
for i in value_array:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zero += 1
print("{:.6f}".format(positive/len(value_array)))
print("{:.6f}".format(negative/len(value_array)))
print("{:.6f}".format(zero/len(value_array)))
