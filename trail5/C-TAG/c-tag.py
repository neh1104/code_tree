n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

# Please write your code here.
ans = 0
seta = set([])
setb = set([])
for x in range(m-2):
    for y in range(x+1, m-1):
        for z in range(y+1, m):
            a = set([]); b = set([])
            for i in range(n):
                sa = A[i]; sb = B[i]
                a.add(sa[x]+sa[y]+sa[z])
                b.add(sb[x]+sb[y]+sb[z])
            if a.isdisjoint(b):
                ans += 1
print(ans)