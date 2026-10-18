n = int(input())
commands = []
x = []
for _ in range(n):
    cmd, val = input().split()
    commands.append(cmd)
    x.append(int(val))

# Please write your code here.

s = set()
for i in range(n):
    c = commands[i]
    num = x[i]
    if c == 'add':
        s.add(num)
    elif c == 'remove':
        s.remove(num)
    else:
        print('true' if num in s else 'false')
