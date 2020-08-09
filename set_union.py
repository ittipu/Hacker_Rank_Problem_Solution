num_of_english = int(input())
value_of_english = set(int(x) for x in input().split())
num_of_french = int(input())
value_of_french = set(int(x) for x in input().split())

num_of_both = len(value_of_english.union(value_of_french))
print(num_of_both)
