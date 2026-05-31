n = int(input())

ch = ord('A')
for _ in range(n):
    for _ in range(n):
        print(chr(ch), end = '')
        ch += 1
    print()
