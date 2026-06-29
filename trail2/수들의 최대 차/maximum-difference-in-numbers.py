N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
arr.sort()
MAX = 0
for i in range(N):
    cnt = 1
    for j in range(i+1, N):
        if abs(arr[i] - arr[j]) <= K:
            cnt += 1
    MAX = max(MAX, cnt)

print(MAX)