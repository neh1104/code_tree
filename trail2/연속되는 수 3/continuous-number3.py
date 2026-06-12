N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
l_n = 0; cnt = 0
MAX = 0
for i in arr:
    if l_n == 0 or (i > 0 and l_n < 0) or (i < 0 and l_n > 0):
        cnt = 1
    else:
        cnt += 1
    l_n = i
    MAX = max(cnt, MAX)

print(MAX)