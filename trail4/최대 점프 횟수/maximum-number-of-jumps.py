n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

vt = [-1 for _ in range(n)]
vt[0] = 0
for i in range(n):
    if vt[i] == -1:
        continue
    for j in range(arr[i]):
        idx = i+j+1
        if idx >= n:
            continue
        if vt[idx] <= vt[i]:
            vt[idx] = vt[i]+1  

print(max(vt))