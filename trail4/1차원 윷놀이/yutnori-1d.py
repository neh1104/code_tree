n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.

lm = sum(nums) // (m-1) 
k = k if k < lm else lm

ls = [0 for _ in range(k)]

MAX = 0
def wornl(curr):
    global MAX
    global ls

    if curr == n:
        MAX = max(MAX, len(list(i for i in ls if i >= m-1)))
        return
    
    for i in range(k):
        ls[i] += nums[curr]
        wornl(curr+1)
        ls[i] -= nums[curr]

wornl(0)
print(MAX)