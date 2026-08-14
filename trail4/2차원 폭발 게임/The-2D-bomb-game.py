n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def drop():
    for i in range(n):
        tmp = [0 for _ in range(n)]
        n_idx = 0
        for j in range(n-1, -1, -1):
            if a[j][i]:
                tmp[n_idx] = a[j][i]
                n_idx += 1
        for j in range(n):
            a[n-1-j][i] = tmp[j]

def rotate():
    global a
    tmp = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            x = j; y = n-i-1
            tmp[x][y] = a[i][j]
    a = tmp
    drop()

def bomb():
    ch = 0
    for i in range(n):
        tmp = []
        lm = 1
        for j in range(1, n):
            if a[j][i] == a[j-1][i]:
                lm += 1
            else:
                if lm >= m and a[j-1][i] != 0:
                    x = 0
                    ch = 1
                else:
                    x = a[j-1][i]
                for _ in range(lm):
                    tmp.append(x)
                lm = 1
        if lm >= m and a[n-1][i] != 0:
            x = 0
            ch = 1
        else:
            x = a[n-1][i]
        for _ in range(lm):
            tmp.append(x)

        for j in range(n):
            a[j][i] = tmp[j]
    drop()
    if ch == 1:
        bomb()

for _ in range(k): #k번 넘게 반복해야할 수도 있음
    bomb()
    rotate()
bomb()

sum = 0
for i in a:
    for j in i:
        if j > 0:
            sum += 1

#for i in a:
#    print(*i)
print(sum)