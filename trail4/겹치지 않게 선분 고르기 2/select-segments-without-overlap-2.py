n = int(input())
x1, x2 = [], []
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

# Please write your code here.

vt = [1 for _ in range(n)]
lines.sort(key = lambda x :(x[0], x[1]))

#bottom-top

for i in range(n):
    a, b = lines[i]
    for j in range(i):
        x1, x2 = lines[j]
        if x2 >= a:
            continue
        vt[i] = max(vt[i], vt[j]+1)

print(max(vt))