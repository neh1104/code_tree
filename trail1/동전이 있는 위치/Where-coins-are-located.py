n, m = map(int, input().split())

a = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    x, y = map(int, input().split())
    a[x-1][y-1] = 1

for i in a:
    print(*i)