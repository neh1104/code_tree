n = int(input())
num = list(map(int, input().split()))

# Please write your code here.

MIN = n+1

def wornl(curr, cnt):
    global MIN
    if cnt >= MIN:
        return

    if curr >= n-1:
        MIN = min(MIN, cnt)
        return    

    a = num[curr]

    for d in range(a, 0, -1):
        #print(a, d)
        wornl(curr+d, cnt+1)

wornl(0, 0)
print(MIN if MIN != n+1 else -1)