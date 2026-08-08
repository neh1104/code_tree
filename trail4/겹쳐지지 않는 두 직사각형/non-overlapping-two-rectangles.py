n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def over():
    return (x1 <= a2 and x2 >= a1) and (y2 >= b1)

def search(c1, r1, c2, r2):
    sum = 0
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            sum += a[r][c]
    return sum

MAX = -100000
for y1 in range(n):
    for x1 in range(m):
        for y2 in range(y1, n):
            for x2 in range(x1, m):
                for b1 in range(y1, n):
                    for a1 in range(m):
                        for b2 in range(b1, n):
                            for a2 in range(a1, m):
                                if over():
                                    continue
                                gon1 = search(x1, y1, x2, y2)
                                gon2 = search(a1, b1, a2, b2)
                                MAX = max(MAX, gon1+gon2)
print(MAX)