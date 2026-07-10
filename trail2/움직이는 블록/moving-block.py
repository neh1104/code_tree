n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
cnt = 0
avg = sum(blocks) // n
for i in range(n):
    cnt += abs(avg-blocks[i])

print(cnt//2)