N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
A = []
for v, t in zip(v, t):
    for i in range(t):
        A.append(0)
        if len(A) == 1:
            A[-1] = v
        else:
            A[-1] = A[-2] + v
B = []
for v, t in zip(v2, t2):
    for i in range(t):
        B.append(0)
        if len(B) == 1:
            B[-1] = v
        else:
            B[-1] = B[-2] + v
al = len(A); bl = len(B)
tup = (0,0); cnt = 0
for i in range(max(al,bl)):
    if i < al:
        a = A[i]
    if i < bl:
        b = B[i]

    if a > b and tup != (1, 0):
        tup = (1, 0)
        cnt += 1
    elif b > a and tup != (0, 1):
        tup = (0, 1)
        cnt += 1
    elif a == b and tup != (1, 1):
        tup = (1, 1)
        cnt += 1
print(cnt)