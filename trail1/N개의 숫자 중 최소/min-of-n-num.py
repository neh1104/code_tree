n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

min = min(a)
cnt = 0

for i in a:
    if i == min:
        cnt += 1

print(min, cnt)