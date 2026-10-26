T = int(input())

for _ in range(T):
    k = int(input())
    operations = [tuple(input().split()) for _ in range(k)]
    command = [op[0] for op in operations]
    n = [int(op[1]) for op in operations]

    # Please write your code here.

    from sortedcontainers import SortedSet
    s = SortedSet()

    for i in range(k):
        c = command[i]
        N = n[i]
        if c == 'I':
            s.add(N)
        elif s:
            if N == 1:
                s.pop(-1)
            else:
                s.pop(0)
    if s:
        print(s[-1], s[0])
    else:
        print('EMPTY')