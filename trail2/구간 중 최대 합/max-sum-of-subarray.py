n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
MAX = -1
for i in range(n-k+1):
    s = sum(arr[i:i+k])
    MAX = max(MAX, s)

print(MAX)