n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.

lm = sum(nums) // (m-1) 
k = k if k < lm else lm

ls = [0 for _ in range(k)]

MAX = 0
def wornl(curr, d):
    
    global MAX
    global ls
    if MAX == lm:
        return

    if curr == n:
        MAX = max(MAX, d)
        return
    
    for i in range(k):
        if ls[i] >= m-1:
            MAX = max(MAX, d)
            continue
            
        ls[i] += nums[curr]
        if ls[i] >= m-1:
            d += 1
        wornl(curr+1, d)
        if ls[i] >= m-1:
            d -= 1
        ls[i] -= nums[curr]

wornl(0, 0)
print(MAX)