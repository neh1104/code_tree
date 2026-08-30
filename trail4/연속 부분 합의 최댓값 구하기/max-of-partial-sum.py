n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

vt = [0 for _ in range(n)]
vt[0] = arr[0]

for i in range(1, n):
    vt[i] = max(vt[i-1]+arr[i], arr[i])

print(max(vt))