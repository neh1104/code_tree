n = int(input())
m = list(map(int, input().split()))

# Please write your code here.

vt = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if m[i]<m[j]:
            vt[i] = max(vt[i], vt[j]+1)


print(max(vt))
