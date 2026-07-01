n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cost = 1000000
for i in range(min(arr), max(arr)+1):
    MIN = i
    MAX = i+k
    sum = 0
    for j in range(n):
        if arr[j] < MIN:
            sum += MIN - arr[j]
        elif arr[j] > MAX:
            sum += arr[j] - MAX
    cost = min(sum, cost)

print(cost)