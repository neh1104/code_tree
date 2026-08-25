n = int(input())

# Please write your code here.
def qnqns():
    for i in range(1, len(ls)//2):
        if ls[-1-i:] == ls[-2-2*i:-1-i]:
            #print(ls[-1-i:], ls[-2-2*i:-1-i])
            return 1
    #print(1)
    return 0


ls = []; MAX = 0
def wornl(curr):
    global ls
    global MAX
    if MAX != 0:
        return

    if qnqns():
        #print(ls, 'not')
        return

    if curr == n:
        #print(ls, 'MAX')
        print(*ls, sep = '')
        MAX = 1
        return

    for i in [4, 5, 6]:
        if len(ls) > 0 and i == ls[-1]:
            continue
        
        ls.append(i)
        wornl(curr+1)
        ls.pop()

wornl(0)