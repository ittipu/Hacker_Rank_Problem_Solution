from collections import Counter

n = int(input())
shoe_size = [int(x) for x in input().split()]
collection = Counter(shoe_size)
customer = int(input())
total_sale = []
for i in range(customer):
    d_size, price = [int(x) for x in input().split()]
    if d_size in collection.keys():
        if collection[d_size] > 0:
            total_sale.append(price)
            collection[d_size] = collection[d_size]-1

print(sum(total_sale))
