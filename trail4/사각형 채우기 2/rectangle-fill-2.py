n = int(input())

# Please write your code here.

memo = [-1 for _ in range(n+1)]

def dp(curr):

    if memo[curr] != -1:
        return memo[curr]
    
    if curr <= 1:
        memo[curr] = 1
    elif curr == 2:
        memo[curr] = 3
    else:
        memo[curr] = (dp(curr-1)+2*dp(curr-2)) % 10007
    return memo[curr]

print(dp(n))
