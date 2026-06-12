n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

MAX = 200
sp = MAX//2
ls = [[
    0 for _ in range(MAX)]
    for _ in range(MAX)
]
ch = 0
for x1, x2, y1, y2 in zip(x1, x2, y1, y2):
    for x in range(x1, x2):
        for y in range(y1, y2):
            ls[x+sp][y+sp] = 1 if ch % 2 == 0 else -1
    ch += 1

cnt = 0
for i in ls:
    cnt += i.count(-1)

print(cnt)