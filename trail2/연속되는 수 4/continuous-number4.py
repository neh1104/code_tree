n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

MAX = 0
for i in range(n):
    if i >= 1 and arr[i-1] < arr[i]:
        cnt += 1
    else:
        cnt = 1
    MAX = max(cnt, MAX)

print(MAX)