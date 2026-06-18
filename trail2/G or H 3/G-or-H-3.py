n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.

def cnt(a):
    s = 0
    for i in a:
        if i == 'G':
            s += 1
        elif i == 'H':
            s += 2
    return s
ls = []
for i in range(max(x)):
    if i+1 in x:
        ls.append(c[x.index(i+1)])
    else:
        ls.append(0)
#print(ls)
MAX = 1
for i in range(len(ls)): 
    a = ls[i:i+k+1]
    S = cnt(a)

    MAX = max(MAX, S)
print(MAX)