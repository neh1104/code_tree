n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.

for _ in range(t):
    ltmp = l[-1]
    for i in range(n-1, 0, -1):
        l[i] = l[i-1]
    l[0] = d[-1]
    rtmp = r[-1]
    for j in range(n-1, 0, -1):
        r[j] = r[j-1]
    r[0] = ltmp
    for k in range(n-1, 0, -1):
        d[k] = d[k-1]
    d[0] = rtmp

print(*l)
print(*r)
print(*d)