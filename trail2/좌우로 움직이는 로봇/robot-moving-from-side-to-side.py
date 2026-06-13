n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
A = []; B = []
for at, ad in zip(t, d):
        for i in range(at):
            A.append(1 if ad == 'R' else -1)
for bt, bd in zip(t_b, d_b):
        for i in range(bt):
            B.append(1 if bd == 'R' else -1)
a = [0,0]; b = [0,0]; cnt = 0
a_m = sum(t); b_m = sum(t_b)
for i in range(max(a_m, b_m)):
    #print(a, b)
    if i < a_m:
        a[1] = a[0]
        a[0] += A[i]
    else:
        a[1] = None
        
    if i < b_m:
        b[1] = b[0]
        b[0] += B[i]
    else:
        b[1] = None

    if a[0] == b[0] and a[1] != b[1]:
        cnt += 1


print(cnt)