n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
ls = []; MAX = 0

def xor(ls):
    now = ls[0]
    for i in ls[1:]:
        now = now ^ i
    return now

def choose(curr, a):
    global MAX
    global ls

    if a > m:
        return

    if curr == n:
        if a != m:
            return
        #print('!')
        MAX = max(MAX, xor(ls))
        return

    #print(curr)

    ls.append(A[curr])
    choose(curr+1, a+1)
    ls.pop()

    choose(curr+1, a)
choose(0, 0)
print(MAX)