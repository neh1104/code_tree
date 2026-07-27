from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)
    
    def empty(self):
        print(1 if not self.dq else 0)
    
    def size(self):
        print(len(self.dq))
    
    def pop(self):
        print(self.dq.popleft())
    
    def front(self):
        print(self.dq[0])

n = int(input())
que = Queue()
for i in range(n):
    a = input()
    if a.startswith('push'):
        a = a.split()
        getattr(que, a[0])(int(a[1]))
    else:
        getattr(que, a)()