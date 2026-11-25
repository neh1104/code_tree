N = int(input())
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]
a, b, c, d = zip(*queries)
a, b, c, d = list(a), list(b), list(c), list(d)

# Please write your code here.

class Node:
  def __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None


def connect(x, y):
  if x is not None:
    x.next = y
  if y is not None:
    y.prev = x


nodes = [None] * (N + 1)
for i in range(1, N + 1):
  nodes[i] = Node(i)
for i in range(1, N):
  connect(nodes[i], nodes[i + 1])

head = nodes[1]

for q in range(Q):
  s1, e1 = nodes[a[q]], nodes[b[q]]
  s2, e2 = nodes[c[q]], nodes[d[q]]

  if e1.next is s2:
    prev1 = s1.prev
    next2 = e2.next
    connect(prev1, s2)
    connect(e2, s1)
    connect(e1, next2)
    if head is s1:
      head = s2
  elif e2.next is s1:
    prev2 = s2.prev
    next1 = e1.next
    connect(prev2, s1)
    connect(e1, s2)
    connect(e2, next1)
    if head is s2:
      head = s1
  else:
    prev1, next1 = s1.prev, e1.next
    prev2, next2 = s2.prev, e2.next
    connect(prev1, s2)
    connect(e2, next1)
    connect(prev2, s1)
    connect(e1, next2)
    if head is s1:
      head = s2
    elif head is s2:
      head = s1

cur = head
out = []
while cur is not None:
  out.append(str(cur.val))
  cur = cur.next
print(" ".join(out))