N = int(input())
commands = []

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

# Please write your code here.
from collections import deque
import heapq

class PQ:

  def __init__(self):
    self.items = []

  def push(self, val):
    # 파이썬 heapq는 최소 힙이므로 최대 힙처럼 쓰기 위해 부호를 반대로 저장합니다.
    heapq.heappush(self.items, -val)

  def pop(self):
    if not self.items:
      return None
    return -heapq.heappop(self.items)

  def size(self):
    return len(self.items)

  def empty(self):
    return 1 if not self.items else 0

  def top(self):
    if not self.items:
      return None
    return -self.items[0]


pq = PQ()

for cmd in commands:
  if cmd[0] == "push":
    pq.push(cmd[1])
  elif cmd[0] == "pop":
    print(pq.pop())
  elif cmd[0] == "size":
    print(pq.size())
  elif cmd[0] == "empty":
    print(pq.empty())
  elif cmd[0] == "top":
    print(pq.top())