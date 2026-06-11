n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

MAX = 200
sp = MAX//2
ls = [[
    0 for _ in range(MAX)]
    for _ in range(MAX)
]

for x1, y1 in zip(x, y):
    for x in range(x1, x1+8):
        for y in range(y1, y1+8):
            ls[x+sp][y+sp] = 1

#print(*ls, sep = '\n')
cnt = 0
for i in ls:
    cnt += i.count(1)

print(cnt)