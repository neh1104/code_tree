n = int(input())
P, L = [], []
for _ in range(n):
    p, l = map(int, input().split())
    P.append(p)
    L.append(l)

m = int(input())
commands = []
for _ in range(m):
    cmd = input().split()
    if cmd[0] == "rc":
        commands.append((cmd[0], int(cmd[1])))
    else:
        commands.append((cmd[0], int(cmd[1]), int(cmd[2])))

# Please write your code here.

from sortedcontainers import SortedSet

s = SortedSet()

for p, l in zip(P, L):
    s.add((l, p))

for c in commands:
    if c[0] == 'rc':
        if c[1] == 1:
            print(s[-1][1])
        else:
            print(s[0][1])
    else:
        if c[0] == 'ad':
            s.add((c[2], c[1]))
        else:
            s.remove((c[2], c[1]))

