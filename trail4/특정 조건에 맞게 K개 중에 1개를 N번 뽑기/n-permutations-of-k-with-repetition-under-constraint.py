K, N = map(int, input().split())

# Please write your code here.
ls = []
def wornl(curr):
    if curr == N:
        print(*ls)
        return
    
    for i in range(1, K+1):
        if len(ls)>=2 and ls[-1] == i and ls[-2] == i:
            continue
        ls.append(i)
        wornl(curr+1)
        ls.pop()

wornl(0)