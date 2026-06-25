n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
def lines(idx, cnr):
    global xlines, ylines
    if cnr == 0:
        xlines.append(idx)
    else:
        ylines.append(idx)

ch = 0
for i in range(11):
    for icnr in range(2):
        for j in range(11):
            for jcnr in range(2):
                for k in range(11):
                    for kcnr in range(2):
                        xlines = []
                        ylines = []
                        lines(i, icnr); lines(j, jcnr); lines(k, kcnr)
                        ls = []
                        for N in range(n):
                            if (x[N] in xlines or y[N] in ylines) and not((x[N], y[N]) in ls):
                                ls.append((x[N], y[N]))
                        if len(ls) == n:
                            ch = 1
                            break

if ch:
    print(1)
else:
    print(0)