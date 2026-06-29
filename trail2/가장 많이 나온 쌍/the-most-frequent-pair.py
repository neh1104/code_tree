n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
MAX = 0
for i in range(m):
    cnt = 1
    for j in range(m):
        if i == j:
            continue
        pi = sorted(pairs[i])
        pj = sorted(pairs[j])
        if pi == pj:
            cnt += 1
    MAX = max(MAX, cnt)

print(MAX)