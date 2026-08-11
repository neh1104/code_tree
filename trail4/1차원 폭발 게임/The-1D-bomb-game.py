n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]

def bomb():
    global a
    ch = 1
    tmp = []
    cnt = 0; y = a[0]
    for x in a:
        if x == y:
            cnt += 1
        else:
            if cnt >= m:
                ch = 0
            else:
                for j in range(cnt):
                    tmp.append(y)
            cnt = 1
            y = x
    if cnt < m:
        for _ in range(cnt):
            tmp.append(y)
    #print(tmp)

    a = tmp
    return ch

while True:
    ch = bomb()
    if ch or not(len(a)):
        break

print(len(a))
for i in a:
    print(i)