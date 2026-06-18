N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
B.sort()
cnt = 0
for i in range(N):
    a = A[i:i+len(B)]
    a.sort()
    if a == B:
        cnt += 1
print(cnt)