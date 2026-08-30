n = int(input())
lines = [tuple(map(int, input().split()))
    for _ in range(n)
]
# Please write your code here.

vt = [1]*n
lines.sort()

#bottom-top

for i in range(n):
    a, _ = lines[i]
    for j in range(i):
        _, x2 = lines[j]
        if x2 < a:
            vt[i] = max(vt[i], vt[j]+1)

print(max(vt))