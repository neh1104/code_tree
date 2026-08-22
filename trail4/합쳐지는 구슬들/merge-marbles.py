n, m, t = map(int, input().split())

r = []
c = []
d = []
w = []

for _ in range(m):
    ri, ci, di, wi = input().split()
    r.append(int(ri))
    c.append(int(ci))
    d.append(di)
    w.append(int(wi))

# Please write your code here.

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
dt = {'U' : 0,
      'L' : 1,
      'D' : 2,
      'R' : 3}
marbles = []
for i in range(m):
    marbles.append((r[i]-1, c[i]-1, dt[d[i]], w[i], i))

isitin = [[-1 for _ in range(n)] for _ in range(n)]
new_marble = []

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def move(marble):
    i, j, d, w, idx = marble
    x = i + dr[d]; y = j + dc[d]
    if in_range(x, y):
        return (x, y, d, w, idx)
    else:
        return (i, j, (d+2)%4, w, idx)

def collide(n_m, o_m):
    x, y, nd, nw, ni = n_m
    _, _, od, ow, oi = o_m
    next_w = nw + ow
    next_d = nd if ni > oi else od
    next_i = ni if ni > oi else oi

    return (x, y, next_d, next_w, next_i)

def push(n_m):
    global isitin
    global new_marble

    x, y, d, w, i = n_m
    if isitin[x][y] == -1:
        new_marble.append(n_m)
        isitin[x][y] = len(new_marble) - 1

    else:
        o_m = new_marble[isitin[x][y]]
        next_m = collide(n_m, o_m)
        new_marble[isitin[x][y]] = next_m


def simulate():
    global marbles
    global new_marble
    global isitin
    for marble in marbles:
        next_marble = move(marble)
        push(next_marble)
    
    marbles = new_marble[:]
    new_marble = []
    isitin = [[-1 for _ in range(n)] for _ in range(n)]

for _ in range(t):
    simulate()

l = len(marbles); idx = 3
MAX = 0
for i in range(l):
    MAX = max(MAX, marbles[i][idx])
print(l, MAX)