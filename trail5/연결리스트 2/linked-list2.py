N = int(input())
Q = int(input())

type_arr = []
i_arr = []
j_arr = []

for _ in range(Q):
    query = list(map(int, input().split()))
    type_arr.append(query[0])
    i_arr.append(query[1])
    if query[0] in [2, 3]:
        j_arr.append(query[2])
    else:
        j_arr.append(0)

# Please write your code here.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

nodes = {i: Node(i) for i in range(1, N + 1)}

def remove(node):
    if node.prev is not None:
        node.prev.next = node.next
    if node.next is not None:
        node.next.prev = node.prev
    node.prev = None
    node.next = None

def insert_prev(target, new_node):
    new_node.next = target
    new_node.prev = target.prev
    if target.prev is not None:
        target.prev.next = new_node
    target.prev = new_node

def insert_next(target, new_node):
    new_node.prev = target
    new_node.next = target.next
    if target.next is not None:
        target.next.prev = new_node
    target.next = new_node

for k in range(Q):
    cmd = type_arr[k]
    i = i_arr[k]
    j = j_arr[k]
    
    if cmd == 1:
        remove(nodes[i])
    elif cmd == 2:
        insert_prev(nodes[i], nodes[j])
    elif cmd == 3:
        insert_next(nodes[i], nodes[j])
    elif cmd == 4:
        target = nodes[i]
        p_val = target.prev.data if target.prev else 0
        n_val = target.next.data if target.next else 0
        print(f"{p_val} {n_val}")

for i in range(1, N + 1):
    n_val = nodes[i].next.data if nodes[i].next else 0
    print(n_val, end=" ")