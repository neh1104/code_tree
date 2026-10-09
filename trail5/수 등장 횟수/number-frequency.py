n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
dt = dict()
for i in arr:
    if i in dt:
        dt[i] += 1
    else:
        dt[i] = 1

for j in nums:
    if j in dt:
        print(dt[j], end = ' ')
    else:
        print(0, end = ' ')