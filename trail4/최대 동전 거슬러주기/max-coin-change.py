N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.

vt = [-1]*(M+1)
vt[0] = 0

coin.sort()
for i in range(M):
    if vt[i] == -1:
        continue
    for c in coin:
        if i+c > M:
            break
        vt[i+c] = max(vt[i]+1, vt[i+c])

print(vt[M])