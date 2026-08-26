n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
vt = [0 for _ in range(n)]; ls = []
MAX = 0
def choose(curr):
    global vt
    global ls
    global MAX
    if curr == n:
        MAX = max(MAX, sum(ls))
        return
    
    for j in range(n):
        if vt[j] == 1:
            continue
        vt[j] = 1
        ls.append(grid[curr][j])
        choose(curr+1)
        vt[j] = 0
        ls.pop()


choose(0)
print(MAX)