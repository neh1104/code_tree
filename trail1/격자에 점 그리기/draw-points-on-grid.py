n, m = map(int, input().split())

a = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1

for i in range(m):
    x, y = map(int, input().split())
    a[x-1][y-1] = num
    num +=1

for ele in a:
    print(*ele)