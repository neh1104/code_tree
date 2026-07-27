from collections import deque

n = int(input())

dq = deque()
for _ in range(n):
    a = input().split()
    if a[0] == 'push_back':
        dq.append(a[1])
    elif a[0] == 'push_front':
        dq.appendleft(a[1])
    elif a[0] == 'pop_front':
        print(dq.popleft())
    elif a[0] == 'pop_back':
        print(dq.pop())
    elif a[0] == 'size':
        print(len(dq))
    elif a[0] == 'empty':
        print(1 if not dq else 0)
    elif a[0] == 'front':
        print(dq[0])
    elif a[0] == 'back':
        print(dq[-1])

