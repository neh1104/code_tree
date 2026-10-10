n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
dt = dict()
for i in arr:
    if i in dt:
        dt[i] += 1
    else:
        dt[i] = 1
cnt = 0
for i in arr:
    if i == k-i and dt[i] >= 2:
        cnt += dt[i]-1
    elif k-i in dt:
        cnt += dt[k-i]

print(cnt//2)