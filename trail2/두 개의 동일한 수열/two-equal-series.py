n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

A.sort(); B.sort()
ch = True
for i in range(n):
    if A[i] != B[i]:
        ch = False
        break

print('Yes' if ch == 1 else 'No')
    
    