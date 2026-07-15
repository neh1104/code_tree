n, m = map(int, input().split())

la = [list(map(int, input().split())) for i in range(n)]
lb = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        if la[i][j] == lb[i][j]:
            print(0, end = ' ')
        else:
            print(1, end = ' ')
    print()