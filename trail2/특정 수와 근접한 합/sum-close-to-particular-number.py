N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
MIN = 10000
for i in range(N):
    for j in range(i+1, N):
        s = sum(arr) - arr[i] - arr[j]
        MIN = min(MIN, abs(S-s))

print(MIN)