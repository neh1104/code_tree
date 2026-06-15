n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
import sys
max = sys.maxsize

for i in range(n):
    sum = 0
    for j in range(n):
        sum += A[j]*abs(i-j)
        
    if sum < max:
        max = sum

print(max)