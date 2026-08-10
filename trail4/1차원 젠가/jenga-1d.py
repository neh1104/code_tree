n = int(input())
a = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def rngpop(s, e):
    global a
    s -= 1; e -= 1
    for i in range(s, e+1):
        a[i] = -1
    
    tmp = []
    for i in a:
        if i != -1:
            tmp.append(i)
    a = tmp

rngpop(s1, e1)
rngpop(s2, e2)

print(len(a))
for i in range(len(a)):
    print(a[i])