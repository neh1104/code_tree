n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# Please write your code here.
MAX = 0
for i in range(3):
    ls = [0]*3
    ls[i] = 1
    cnt = 0
    for j in range(n):
        tmp = ls[a[j]-1]
        ls[a[j]-1] = ls[b[j]-1]
        ls[b[j]-1] = tmp
        if ls[c[j]-1] == 1:
            cnt += 1
    MAX = max(MAX, cnt)

print(MAX)