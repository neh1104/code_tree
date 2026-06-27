inp = [input() for _ in range(3)]

# Please write your code here.

dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]

def in_range(x, y):
    return 0<=x<3 and 0<=y<3

def cross(arr):
    global num_ls
    ls = []
    for i in arr:
        if not(i in ls):
            ls.append(i)
    ls.sort()
    ls = "".join(ls)
    
    if len(ls) == 2 and not(ls in num_ls):
        #print(ls)
        num_ls.append(ls)

cnt = 0
num_ls = []
for x in range(3):
    for y in range(3):

        for d in range(4): #direction
            ls = []
            for l in range(3): #length
                if in_range(x+dx[d]*l, y+dy[d]*l):
                    ls.append(inp[x+dx[d]*l][y+dy[d]*l])
                    if len(ls) == 3:
                        cross(ls)
                                 
                else:
                    break
#print(num_ls)
print(len(num_ls))