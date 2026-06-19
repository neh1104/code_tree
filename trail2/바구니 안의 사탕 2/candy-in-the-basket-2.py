N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
n = max(pos)
ls = [0]*(n)

for i in range(len(pos)):
    ls[pos[i]-1] += candy[i]

#print(ls)
MAX = 0
for i in range(len(ls)):
    S = sum(ls[i:i+2*K+1])
    #print(ls[i:i+2*K+1])
    MAX = max(MAX,S)

print(MAX)