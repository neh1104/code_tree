n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

dt = dict()
for i in arr:
    dt[i] = dt.get(i, 0) + 1

cnt = 0
for i in range(n):
    dt[arr[i]] -= 1
    for j in range(i+1, n):
        dt[arr[j]] -= 1
        target = k-arr[i]-arr[j]
        if target in dt:
            cnt += dt[target]
        dt[arr[j]] += 1
print(cnt//2)