n = int(input())
command = []
x = []

for _ in range(n):
    line = input().split()
    command.append(line[0])
    if line[0] in ["add", "remove", "find", "lower_bound", "upper_bound"]:
        x.append(int(line[1]))
    else:
        x.append(0)

# Please write your code here.

from sortedcontainers import SortedSet
s = SortedSet()

for i in range(n):
    c = command[i]
    N = x[i]
    if c == 'add':
        s.add(N)
    elif c == 'remove':
        s.remove(N)
    
    elif c == 'find':
        print('true' if N in s else 'false')

    elif c == 'lower_bound':
        X = s.bisect_left(N)
        print(s[X] if X < len(s) else 'None')
    elif c == 'upper_bound':
        X = s.bisect_right(N)
        print(s[X] if X < len(s) else 'None')

    else:
        if not s:
            print('None')
        elif c == 'largest':
            print(s[-1])
        else:
            print(s[0])