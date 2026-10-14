n = int(input())

cmd = []
k = []
v = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] == "add":
        k.append(int(line[1]))
        v.append(int(line[2]))
    elif line[0] == "remove" or line[0] == "find":
        k.append(int(line[1]))
        v.append(0)
    else:
        k.append(0)
        v.append(0)

# Please write your code here.

from sortedcontainers import SortedDict

dt = SortedDict()

for i in range(n):
    CMD = cmd[i]
    if CMD == 'add':
        dt[k[i]] = v[i]
    elif CMD == 'remove':
        dt.pop(k[i])
    elif CMD == 'find':
        print(dt.get(k[i], 'None'))
    else:
        print(*dt.values()) if dt else print('None')
