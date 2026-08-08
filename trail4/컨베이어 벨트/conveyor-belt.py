n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ab = a+b
for _ in range(t):
    tmp = ab[-1] 
    for i in range(2*n-1, 0, -1):
        ab[i] = ab[i-1]
    ab[0] = tmp

print(*ab[:n])
print(*ab[n:])