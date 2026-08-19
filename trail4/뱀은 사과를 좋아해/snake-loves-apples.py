n, M, K = map(int, input().split())

x, y = [], []
for _ in range(M):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

d, p = [], []
for _ in range(K):
    di, pi = input().split()
    d.append(di)
    p.append(int(pi))

# Please write your code here.

a = [[0 for _ in range(n)] for _ in range(n)]
#사과 추가 
for i, j in zip(x, y):
    a[i-1][j-1] = -1
a[0][0] = 1

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
dt = {'L' : 0,
      'R' : 1,
      'U' : 2,
      'D' : 3}

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def move(d):
    global mls
    global a
    
    headr = mls[0][0]+dr[d]
    headc = mls[0][1]+dc[d]
    #격자 탈출
    if in_range(headr, headc) == 0:
        return 0
    
    mls.insert(0, (headr, headc))
    tailr, tailc = mls.pop()
    a[tailr][tailc] = 0
    
    #사과
    if a[headr][headc] == -1:
        a[headr][headc] = 1
        a[tailr][tailc] = 1
        mls.append((tailr, tailc))
        return 1
    #공백
    elif a[headr][headc] == 0:
        a[headr][headc] = 1
        return 1
    #꼬임
    else:
        return 0

    return 1

t = 0
mls = [(0, 0)]
for D, p in zip(d, p):
    d = dt[D]
    for _ in range(p):
        canmove = move(d)
        t += 1
        #print(*a, sep = '\n')
        #print()
        if not(canmove):
            break

    if not(canmove):
        break
print(t)