n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

# Please write your code here.

ls = [0]*101

for L, R in zip(l, r):
    for i in range(L, R+1):
        ls[i] += 1

#print(ls)
cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            LS = ls.copy()
            #print(i, j, k)
            for id in [i, j, k]:
                #print(id)
                L = l[id]
                R = r[id]
                #print(L, R)
                for a in range(L, R+1):
                    LS[a] -= 1
            ch = 1
            for lsi in LS:
                if lsi >= 2:
                    ch = 0
                    break
            if ch:
                cnt += 1

print(cnt)