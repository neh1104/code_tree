n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# Please write your code here.
a = ord('A')
ls = [chr(a+i) for i in range(n)]
def wish(i):
    copy = ls[::]
    for j in range(i, m):
        if c[j] in copy:
            copy.remove(c[j])
    return copy

last = []
for i in range(m):
    if i == 0 or u[i] != u[i-1]:
        last = wish(i)
    if i == p-1:
        if u[i] == 0:
            break
        print(*last)
        break
