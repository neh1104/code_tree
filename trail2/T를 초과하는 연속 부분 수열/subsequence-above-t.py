n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

MAX = 0; cnt = 0
for i in range(n):
    if arr[i] > t:
        cnt += 1
    else:
        cnt = 0
    MAX = max(cnt,MAX)

print(MAX)