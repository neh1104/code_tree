n = int(input())

for i in range(n):
    for j in range(n):
        print((i+1)*(n-j), end = ' ')
    print()