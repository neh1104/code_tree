n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

A = []
for d, i in zip(v, t):
    for i in range(i):
        A.append(d)

B = []
for d, i in zip(v2, t2):
    for i in range(i):
        B.append(d)

a_m = 0; b_m = 0; head = 0
for i in range(sum(t)):
    a_m += A[i]; b_m += B[i]

    if head == 0:
        cnt = 0
        if a_m == b_m:
            head = 0
            cnt =0
        elif a_m > b_m:
            head = 'A'
        else:
            head = 'B'
    if a_m > b_m and head == 'B':
        cnt += 1
        head = 'A'
    elif a_m < b_m and head == 'A':
        cnt += 1
        head = 'B'

print(cnt)