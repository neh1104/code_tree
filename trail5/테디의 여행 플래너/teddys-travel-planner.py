N, Q = map(int, input().split())
cities = list(input().split())
option = []
new_city = [None] * Q
for i in range(Q):
    query = input().split()
    option.append(int(query[0]))
    if option[i] == 4:
        new_city[i] = query[1]

# Please write your code here.
class Node:
    def __init__(self, name):
        self.name = name
        self.prev = None
        self.next = None

nodes = {}
head = None
tail = None

for name in cities:
    node = Node(name)
    nodes[name] = node
    if head is None:
        head = node
        tail = node
    else:
        tail.next = node
        node.prev = tail
        tail = node

if head is not None and tail is not None:
    tail.next = head
    head.prev = tail

cur = head

for i in range(Q):
    op = option[i]

    if op == 1:
        if cur.next is not None:
            cur = cur.next
    elif op == 2:
        if cur.prev is not None:
            cur = cur.prev
    elif op == 3:
        target = cur.next
        if target is not None and target is not cur:
            nxt = target.next
            cur.next = nxt
            nxt.prev = cur
            nodes.pop(target.name, None)
    elif op == 4:
        name = new_city[i]
        new_node = Node(name)
        nodes[name] = new_node
        nxt = cur.next
        cur.next = new_node
        new_node.prev = cur
        new_node.next = nxt
        nxt.prev = new_node

    left_name = cur.prev.name if cur.prev is not None else None
    right_name = cur.next.name if cur.next is not None else None

    if left_name is None or right_name is None or left_name == right_name:
        print(-1)
    else:
        print(left_name, right_name)