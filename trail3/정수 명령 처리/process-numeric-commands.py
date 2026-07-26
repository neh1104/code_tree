class Stack:
    def __init__(self):
        self.st = []
    def push(self, A):
        self.st.append(A)
    def pop(self):
        print(self.st.pop())
    def size(self):
        print(len(self.st))
    def empty(self):
        print(1 if not self.st else 0)
    def top(self):
        print(self.st[-1])

n = int(input())
st = Stack()

for i in range(n):
    a = input().split()
    if a[0] == 'push':
        st.push(int(a[-1]))
    elif a[0] == 'pop':
        st.pop()
    elif a[0] == 'size':
        st.size()
    elif a[0] == 'empty':
        st.empty()
    else:
        st.top()
