a = [list(map(int, input().split())) for _ in range(4)]
dir = input()

def combination(tmp):
    ls = [0 for _ in range(4)]
    n = 0
    for i in range(4):
        if i != 3 and tmp[i] == tmp[i+1]:
            tmp[i+1] = 0
            tmp[i] *= 2
        if tmp[i] != 0:
            ls[n] = tmp[i]
            n += 1
    return ls
        
def blow():
    for i in range(4):
        tmp = [0 for _ in range(4)]
        n = 0
        for j in range(4):
            if dir == 'L':
                x = i; y = j
            elif dir == 'R':
                x = i; y = 3-j
            elif dir == 'U':
                x = j; y = i
            else:
                x = 3-j; y = i
            
            if a[x][y] != 0:
                tmp[n] = a[x][y]
                n += 1

        tmp = combination(tmp)
        #print(tmp)
        for j in range(4):
            if dir == 'L':
                x = i; y = j
            elif dir == 'R':
                x = i; y = 3-j
            elif dir == 'U':
                x = j; y = i
            else:
                x = 3-j; y = i
            a[x][y] = tmp[j]

blow()
for i in a:
    print(*i)