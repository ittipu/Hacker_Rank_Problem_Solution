def solve(s):
    for char in s.split():
        print(char)
        s = s.replace(char, char.capitalize())
    return s


if __name__ == '__main__':
    s = input()
    print(solve(s))
