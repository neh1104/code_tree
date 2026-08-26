n = int(input())

# Please write your code here.
visited = [0 for i in range(n+1)]
ls = []
def choose(curr):
    global ls
    global visited

    if curr == n:
        print(*ls)
        return
    
    for i in range(1, n+1):
        if visited[i] == 1:
            continue
        visited[i] = 1
        ls.append(i)
        choose(curr+1)
        visited[i] = 0
        ls.pop()


choose(0)