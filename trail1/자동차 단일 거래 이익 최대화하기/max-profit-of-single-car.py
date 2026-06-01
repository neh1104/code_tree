n = int(input())
p = list(map(int, input().split()))

# Please write your code here.
mpr = 0
for j in range(1, n):
    mn = p[j-1]
    for i in range(j):
        if p[i] < mn:
            mn = p[i]
    
    pri = p[j] - mn
    if mpr < pri:
        mpr = pri
print(mpr)

        
