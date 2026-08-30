n, m = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(n)]
s = [x[0] for x in clothes]
e = [x[1] for x in clothes]
v = [x[2] for x in clothes]

# Please write your code here.
import sys
INT_MIN = -sys.maxsize

vt = [[INT_MIN for _ in range(n)] for _ in range(m+1)]
for i in range(n):
    if s[i]<=1<=e[i]:
        vt[1][i] = 0

for i in range(2, m+1):
    for j in range(n):
        if s[j]<=i<=e[j]:
            for diff in range(n):
                if vt[i-1][diff] == INT_MIN:
                    continue
                vt[i][j] = max(vt[i-1][diff]+abs(v[j]-v[diff]), vt[i][j])

#print(*vt, sep = '\n')
print(max(vt[m]))