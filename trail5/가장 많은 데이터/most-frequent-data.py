n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.

dt = dict()

for i in words:
    if i in dt:
        dt[i] += 1
    else:
        dt[i] = 1

print(max(dt.values()))