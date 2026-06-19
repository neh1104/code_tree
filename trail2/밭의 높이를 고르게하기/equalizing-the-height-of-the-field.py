N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
MIN = 200*10

for i in range(N-T+1):
    S = 0
    for j in range(T):
        S += abs(arr[i+j] - H)
    MIN = min(MIN, S)

print(MIN)