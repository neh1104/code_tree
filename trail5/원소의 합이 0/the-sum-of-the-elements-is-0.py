n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# Please write your code here.
da, db, dc, dd = dict(), dict(), dict(), dict()

for a, b, c, d in zip(A, B, C, D):
    da[a] = da.get(a, 0) + 1
    db[b] = db.get(b, 0) + 1 
    dc[c] = dc.get(c, 0) + 1 
    dd[d] = dd.get(d, 0) + 1 

ab = dict()
for a in da:
    for b in db:
        ab[a+b] = ab.get(a+b, 0) + da[a]*db[b]

cd = dict()
for c in dc:
    for d in dd:
        cd[c+d] = cd.get(c+d, 0)+ dc[c]*dd[d]

cnt = 0
for i in ab:
    cnt += cd.get(-i, 0)*ab[i]

print(cnt)