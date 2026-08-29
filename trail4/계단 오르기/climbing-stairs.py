n = int(input())

# Please write your code here.
memo = [-1 for _ in range(n+1)]

def dp(curr):
    if memo[curr] != -1:
        return memo[curr] 
    if curr == 1:
        return 0

    if curr <= 3:
        memo[curr] = 1
    else:
        memo[curr] = dp(curr-2)+dp(curr-3)

    return memo[curr]

print(dp(n)%10007)
