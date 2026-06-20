n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.
MAX = 0
for i in range(n):
    ls = [0]*1000
    for j in range(n):
        if i == j:
            continue
        A = a[j]; B = b[j]
        for k in range(A, B):
            ls[k] += 1
    MAX = max(MAX, 1000-ls.count(0))

print(MAX)