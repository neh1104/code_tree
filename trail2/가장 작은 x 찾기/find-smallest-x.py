n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.
N = 1
i = 0
while True:
    ch = 1
    for j in range(n):
        if not(a[j]<=N*(2**(j+1))<=b[j]):
            ch = 0
            break
    if ch:
        print(N)
        break
    N += 1

