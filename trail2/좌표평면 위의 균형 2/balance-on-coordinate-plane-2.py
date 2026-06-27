n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
MIN = 100
for x in range(2, 100, 2):
    for y in range(2, 100, 2):
        ls = [0]*4
        for p in points:
            px = p[0]; py = p[1]

            if px > x and py > y:
                ls[0] += 1
            elif px > x and py < y:
                ls[1] += 1
            elif py < y:
                ls[2] += 1
            else:
                ls[3] += 1
        MIN = min(MIN, max(ls))

print(MIN)