n, m = map(int, input().split())
s = input()

commands = []
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        commands.append((cmd[0],))
    else:
        commands.append((cmd[0], cmd[1]))

# Please wrself.ite your code here.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLLt:
    def __init__(self):
        # 1. 양 끝에 가짜 노드를 만들어 벽을 세웁니다.
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # 2. iterator(it)는 처음에 맨 뒤(tail)를 가리킵니다.
        self.it = self.tail

    def P(self, new_data):
        # 항상 현재 self.it의 '바로 앞'에 새 노드를 삽입합니다.
        new_node = Node(new_data)
        
        new_node.prev = self.it.prev
        new_node.next = self.it
        
        self.it.prev.next = new_node
        self.it.prev = new_node

    def m(self, a):
        # 초기 문자열을 넣는 것도 결국 '맨 뒤(tail)에서 P를 연속으로 하는 것'과 같습니다!
        for i in a:
            self.P(i)

    def L(self):
        # 맨 앞 더미(head)가 아닐 때만 왼쪽으로 이동
        if self.it.prev != self.head:
            self.it = self.it.prev

    def R(self):
        # 맨 뒤 더미(tail)가 아닐 때만 오른쪽으로 이동
        if self.it != self.tail:
            self.it = self.it.next

    def D(self):
        # 맨 뒤(tail)가 아니라면, 가리키는 위치 바로 뒤(self.it)의 노드를 제거합니다.
        # 더미 구조에서는 self.it가 가리키는 노드가 곧 '바로 뒤의 빵'이 됩니다.
        if self.it != self.tail:
            target = self.it
            self.it = target.next # iterator를 미리 다음으로 옮겨둡니다.
            
            target.prev.next = self.it
            self.it.prev = target.prev

    def print_all(self):
        # head 다음부터 tail 전까지 출력하면 정답이 됩니다.
        curr = self.head.next
        while curr != self.tail:
            print(curr.data, end="")
            curr = curr.next
        print()

DLL = DLLt()
DLL.m(s)

for i in range(m):
    if commands[i][0] == 'L':
        DLL.L()
    elif commands[i][0] == 'R':
        DLL.R()
    elif commands[i][0] == 'D':
        DLL.D()
    else:
        DLL.P(commands[i][1])

DLL.print_all()
