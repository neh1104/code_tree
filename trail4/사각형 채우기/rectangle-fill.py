n = int(input())

# Please write your code here.
memo = [-1 for _ in range(n+1)]
def dp(curr):
    if memo[curr] != -1:
        return memo[curr]

    if curr <= 3:
        memo[curr] = curr
    else:
        memo[curr] = dp(curr-1)+dp(curr-2)
    return memo[curr]

print(dp(n)%10007)