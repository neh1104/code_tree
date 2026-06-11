n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
d_ls = []
s_p = 1000*100
for i, d in zip(x, dir):
    if d == 'R':
        l_p = s_p 
        r_p = s_p + i
        s_p = r_p -1
        a = 1
    else:
        r_p = s_p + 1
        l_p = s_p - i + 1
        s_p = l_p
        a = -1
    d_ls.append([l_p, r_p, a])

ls = [[0, 0, 2] for _ in range(1000*100*2)]
for l, r, a in d_ls:
    if a == 1:
        for i in range(l, r):
            if ls[i][0] <= -2 and ls[i][1] == 1:
                ls[i][2] = 0
            elif ls[i][2] != 0:
                ls[i][1] += 1
                ls[i][2] = 1
            
    else:
        for i in range(l, r):
            if ls[i][0] == -1 and ls[i][1] >= 2:
                ls[i][2] = 0
            elif ls[i][2] != 0:
                ls[i][0] -= 1
                ls[i][2] = -1
    #print(ls)

#print(ls)
w, b, g = 0, 0, 0
for i in ls:
    if i[2] == 0:
        g += 1
    elif i[2] == 1:
        b += 1
    elif i [2] == -1:
        w += 1
print(w, b, g)