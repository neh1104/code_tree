n = int(input())
m = list(map(int, input().split()))

# Please write your code here.

vt = [-1 for _ in range(n)]
vt[0] = 1
for i in range(1, n):
    MAX = 0
    for j in range(i):
        if m[j] >= m[i]:
            continue
        if vt[j] > MAX:
            MAX = vt[j]
    
    vt[i] = MAX+1


print(max(vt))