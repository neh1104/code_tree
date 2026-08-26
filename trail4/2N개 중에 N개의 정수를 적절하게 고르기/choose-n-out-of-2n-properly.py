n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
s = sum(num)
MIN = 999999
def choose(curr, a, d):
    global MIN
    if d == n:
        MIN = min(MIN, abs(a - abs(s-a)))
        return

    if curr == 2*n:
        if d != n:
            return
        MIN = min(MIN, abs(a-abs(s-a)))
        return
    
    k = num[curr]
        
    choose(curr+1, a+k, d+1)

    choose(curr+1, a, d)
    
choose(0, 0, 0)
print(MIN)