T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Please write your code here.
X = max(x)
ls = [0]*X
for i in range(T):
    ls[x[i]-1] = c[i]
#print(ls) 

def find_c():
    ls_s = X
    ls_n = X
    for x in range(X):
        if ls[x] == 'S':
            ls_s = min(ls_s, abs(x-i))
        if ls[x] == 'N':
            ls_n = min(ls_n, abs(x-i))
    return True if ls_s <= ls_n else False


cnt = 0
for i in range(a-1, b):
    if find_c():
        cnt += 1

print(cnt)