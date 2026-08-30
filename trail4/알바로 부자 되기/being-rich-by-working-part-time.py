n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]

# Please write your code here.
#top_down
vt = [0 for _ in range(n)]

def dp(curr):
    if vt[curr] != 0:
        return vt[curr]
    price = p[curr]
    vt[curr] = price
    for i in range(curr+1, n):
        if s[i] > e[curr]:
            vt[curr] = max(vt[curr], dp(i)+price) 
    return vt[curr]

print(max(dp(i) for i in range(n)))