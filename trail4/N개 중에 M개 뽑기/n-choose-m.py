N, M = map(int, input().split())

# Please write your code here.
ls = []
def choose(curr, last):
    global ls

    if curr == M:
        print(*ls) 
        return
    
    for i in range(1, N+1):
        if i <= last:
            continue
        ls.append(i)
        choose(curr + 1, i)
        ls.pop()
    
choose(0, 0)