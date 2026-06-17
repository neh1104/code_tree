A = input()

# Please write your code here.
n = len(A)
cnt = 0
for i in range(n-3):
    if A[i]+A[i+1] == '((':
        for j in range(i+2, n-1):
            if A[j]+A[j+1] == '))':
                cnt += 1

print(cnt)