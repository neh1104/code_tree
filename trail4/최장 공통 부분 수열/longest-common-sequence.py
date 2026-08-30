A = input()
B = input()

# Please write your code here.

n = len(A)
m = len(B)

vt = [[0 for _ in range(m)] for _ in range(n)]

if A[0] == B[0]:
    vt[0][0] = 1
    cha = 0
    chb = 0
else:
    cha = 1
    chb = 1

for i in range(1, n):
    if cha and A[i] == B[0]:
        vt[i][0] = vt[i-1][0] + 1
        cha = 0
    else:
        vt[i][0] = vt[i-1][0]

for i in range(1, m):
    if chb and B[i] == A[0]:
        vt[0][i] = vt[0][i-1] + 1
        chb = 0
    else:
        vt[0][i] = vt[0][i-1]

for i in range(1, n):
    for j in range(1, m):
        if A[i] == B[j]:
            vt[i][j] = vt[i-1][j-1] + 1
        else:
            vt[i][j] = max(vt[i-1][j], vt[i][j-1])

print(vt[n-1][m-1])