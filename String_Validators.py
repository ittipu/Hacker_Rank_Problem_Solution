if __name__ == '__main__':
    S = input()
    for ch in S:
        print(any(ch.isalpha()))
    print(any(char.isalnum() for char in S))
    print(any(char.isalpha() for char in S))
    print(any(char.isdigit() for char in S))
    print(any(char.islower() for char in S))
    print(any(char.isupper() for char in S))
