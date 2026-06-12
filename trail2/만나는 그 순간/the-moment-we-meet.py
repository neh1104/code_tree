n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
A = []
for d, i in zip(d, t):
    if d == 'R':
        for j in range(i):
            A.append(1)
    else:
        for j in range(i):
            A.append(-1)

B = []
for d, i in zip(d2, t2):
    if d == 'R':
        for j in range(i):
            B.append(1)
    else:
        for j in range(i):
            B.append(-1)

a_move = 0; b_move = 0
i = 0
while True:
    if i == len(A) and a_move != b_move:
        print(-1)
        break
    a_move += A[i]
    b_move += B[i]
    i += 1
    if a_move == b_move:
        print(i)
        break 