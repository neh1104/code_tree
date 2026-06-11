x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.

MAX = 2000
sp = MAX //2

ls = [
    [0 for _ in range(MAX)]
    for _ in range(MAX)
]

for i in range(3):
    for x in range(x1[i], x2[i]):
        for y in range(y1[i], y2[i]):
            ls[x][y] = 1 if i != 2 else 0

cnt = 0
for i in ls:
    cnt += i.count(1)

print(cnt)