n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

u = sequence[:]
d = list(reversed(u))
udx = [1 for _ in range(n)]
ddx = [1 for _ in range(n)]

def bottom_top(ls, idx):
    for i in range(n):
        for j in range(i):
            if ls[j] < ls[i]:
                idx[i] = max(idx[j]+1, idx[i])

bottom_top(u, udx)
bottom_top(d, ddx)
#print(udx)
#print(ddx)
MAX = 0
for i in range(n):
    uMAX = max(udx[:i+1])
    dMAX = max(ddx[:n-i])
    #print(uMAX, dMAX)
    MAX = max(MAX, uMAX+dMAX)

print(MAX-1)