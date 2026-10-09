n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
        
    else:
        commands.append((cmd, k))

# Please write your code here.
dt = dict()
for i in commands:
    if i[0] == 'add':
        dt[i[1]] = i[2]
    elif i[0] == 'remove':
        dt.pop(i[1])
    else:
        print(dt[i[1]] if i[1] in dt else 'None')

