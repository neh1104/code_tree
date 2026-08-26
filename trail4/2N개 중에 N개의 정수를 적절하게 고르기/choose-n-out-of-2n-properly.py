n = int(input())
num = list(map(int, input().split()))

# Please write your code here.

MIN = 999999
def choose(curr, a, b, d):
    global MIN
    if curr == 2*n:
        if d != n:
            return
        #print(a, b)
        MIN = min(MIN, abs(a-b))
        return
    
    k = num[curr]
    if d == n:
        choose(curr+1, a, b+k, d)
    else:
        choose(curr+1, a+k, b, d+1)

        choose(curr+1, a, b+k, d)
choose(0, 0, 0, 0)
print(MIN)