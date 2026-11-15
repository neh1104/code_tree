S_init = input()
N = int(input())
command = []
S_value = []
for _ in range(N):
    line = input().split()
    cmd = int(line[0])
    command.append(cmd)
    if cmd == 1 or cmd == 2:
        S_value.append(line[1])
    else:
        S_value.append("")
# Please write your code here.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insert_prev(cur, data):
    new_node = Node(data)
    new_node.prev = cur.prev
    new_node.next = cur
    if cur.prev is not None:
        cur.prev.next = new_node
    cur.prev = new_node

def insert_next(cur, data):
    new_node = Node(data)
    new_node.prev = cur
    new_node.next = cur.next
    if cur.next is not None:
        cur.next.prev = new_node
    cur.next = new_node

def print_nodes(cur):
    prev_str = cur.prev.data if cur.prev is not None else "(Null)"
    curr_str = cur.data
    next_str = cur.next.data if cur.next is not None else "(Null)"
    print(f"{prev_str} {curr_str} {next_str}")

cur = Node(S_init)

for i in range(N):
    cmd = command[i]
    val = S_value[i]
    
    if cmd == 1:
        insert_prev(cur, val)
    elif cmd == 2:
        insert_next(cur, val)
    elif cmd == 3:
        if cur.prev is not None:
            cur = cur.prev
    elif cmd == 4:
        if cur.next is not None:
            cur = cur.next
            
    print_nodes(cur)