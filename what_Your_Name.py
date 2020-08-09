def print_full_name(a, b):
    newText="Hello {} {}! You just delved into python.".format(a,b)
    print(newText)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
