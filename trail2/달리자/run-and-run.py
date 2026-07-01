n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(n):
    while A[i] > B[i]:
        cnt += 1
        A[i]-=1
        A[i+1]+=1

print(cnt)