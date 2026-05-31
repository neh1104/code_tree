n = int(input())

for i in range(n):
    for j in range(i, -1, -1):
        print(n-j, end = ' ')
    print()