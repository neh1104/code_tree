k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Please write your code here.
cnt = 0
for i in range(1, 1+n):
    for j in range(1, 1+n):
        if i == j:
            continue

        ch = 1
        for a in arr:
            if a.index(i) > a.index(j):
                ch = 0
                break
        if ch:
            cnt += 1
            #print(i, j)

print(cnt)