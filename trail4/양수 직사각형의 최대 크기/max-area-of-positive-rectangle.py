n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
MAX = -1
for i in range(n):
    for j in range(m):
        for r in range(n-i):
            for c in range(m-j):
                sum = 0; ch = 0
                for row in range(r+1):
                    for col in range(c+1):
                        if a[i+row][j+col] > 0:
                            sum += 1
                        else:
                            ch = 1
                    if ch:
                        sum = -1
                        break
                MAX = max(MAX, sum)
                

print(MAX)