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
for i in range(n):
    dt[arr[i]] -= 1
    for j in range(i+1, n):
        dt[arr[j]] -= 1
        target = k-arr[i]-arr[j]
        cnt += dt[target] if target in dt else 0
        dt[arr[j]] += 1

print(cnt//2)