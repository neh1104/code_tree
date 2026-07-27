n, k = map(int, input().split())

# Please write your code here.

from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)
    
    def empty(self):
        return(1 if not self.dq else 0)
    
    def size(self):
        return(len(self.dq))
    
    def pop(self):
        return(self.dq.popleft())
    
    def front(self):
        return(self.dq[0])

que = Queue()
for i in range(1, n+1):
    que.push(i)
ls = []
while que.size() != 0:
    for i in range(k-1):
        que.push(que.front())
        que.pop()
    ls.append(que.pop())

print(*ls)