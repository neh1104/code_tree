n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.

dt = dict()

for i in words:
    i = list(i)
    i.sort()
    i = ''.join(i)
    dt[i] = dt.get(i, 0) + 1

print(max(dt.values()))