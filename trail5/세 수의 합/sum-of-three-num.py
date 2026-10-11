n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

dt = dict()
for i in arr:
    dt[i] = dt.get(i, 0) + 1

cnt = 0
for i in range(n):
    dt[arr[i]] -= 1
    for j in range(i):

        target = k-arr[i]-arr[j]
        cnt += dt.get(target, 0)

print(cnt)