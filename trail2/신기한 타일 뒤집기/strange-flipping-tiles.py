n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
max = 1000*100
ls = [0]*2*(max)
sp = max
for i, d in zip(x, dir):
    if d == 'R':
        for j in range(sp, sp+i):
            ls[j] = 1
        sp += i - 1
    else:
        for j in range(sp, sp-i, -1):
            ls[j] = -1
        sp = sp - i + 1
#print(ls)
b = ls.count(1); w = ls.count(-1)

print(w, b)