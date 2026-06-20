n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
cnt = 0
for i in range(n):
    ch = 1
    for j in range(n):
        if i == j:
            continue
        x1 = lines[i][0]-lines[j][0]
        x2 = lines[i][1]-lines[j][1]
        if x1*x2 < 0:
            ch = 0
            break
    if ch:
        cnt += 1

print(cnt)