A = input()
B = input()

# Please write your code here.

n = len(A)
m = len(B)

vt = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i-1] == B[j-1]:
            vt[i][j] = vt[i-1][j-1] + 1
        else:
            vt[i][j] = max(vt[i-1][j], vt[i][j-1])

#print(*vt, sep = '\n')
print(vt[n][m])
