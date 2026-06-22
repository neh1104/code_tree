X, Y = map(int, input().split())

# Please write your code here.

MAX = 0
for i in range(X, Y+1):
    sum = 0
    for j in str(i):
        sum += int(j)
    MAX = max(MAX, sum)
print(MAX)