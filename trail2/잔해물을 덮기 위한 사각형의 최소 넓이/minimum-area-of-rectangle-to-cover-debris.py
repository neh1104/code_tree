x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

ls = [
    [0 for i in range(2005)]
    for i in range(2005)
]
p = 1000
for x in range(x1[0], x2[0]):
    for y in range(y1[0], y2[0]):
        ls[x+p][y+p] = 1

for x in range(x1[1], x2[1]):
    for y in range(y1[1], y2[1]):
        ls[x+p][y+p] = 0

#print(*ls, sep = '\n')
min_x, min_y, max_x, max_y = 3000, 3000, -1, -1

for i in range(2005):
    for j in range(2005):
        if ls[i][j] == 1:
            if i < min_x:
                min_x = i
            if i > max_x:
                max_x = i
            if j < min_y:
                min_y = j
            if j > max_y:
                max_y = j

print(0 if (min_x, min_y) == (3000,3000) and (max_x, max_y) == (-1, -1) else (max_x-min_x+1)*(1+max_y-min_y))