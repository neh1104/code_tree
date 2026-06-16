n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if A[k] >= A[j] >= A[i]:
                cnt += 1
print(cnt)