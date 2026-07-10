n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

cnt = 0
p = 0
for i in range(n):
    move = p + i
    if move >= n:
        break
    
    if arr[move] == 1:
        cnt += 1
        p += 2*m

print(cnt)