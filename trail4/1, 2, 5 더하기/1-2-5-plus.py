n = int(input())

# Please write your code here.

vt = [0 for _ in range(n+1)]
vt[0] = 1

for i in range(n):
    if vt[i] == 0:
        continue
    for l in [1, 2, 5]:
        if i + l > n:
            continue
        vt[i+l] += vt[i]

print(vt[n]%10007)
