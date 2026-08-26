n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

MAX = 0; min_ls = []
def find_min(curr, d):
    global MAX
    global min_ls
    if d == 2:
        m1 = min_ls[0]; m2 = min_ls[1]
        #print(m1, m2)
        MAX = max(MAX, (m1[0]-m2[0])**2 + (m1[1]-m2[1])**2)
        return

    if curr == m:
        return

    min_ls.append(ls[curr])
    find_min(curr+1, d+1)
    min_ls.pop()

    find_min(curr+1, d)
    return MAX
    
ls = []; result = []
def choose(curr, d):
    global ls
    global result
    global MAX
    if d == m:
        MAX = 0
        result.append(find_min(0, 0))
        return

    if curr == n:
        return

    ls.append(points[curr])
    choose(curr+1, d+1)
    ls.pop()

    choose(curr+1, d)

choose(0, 0)
print(min(result))