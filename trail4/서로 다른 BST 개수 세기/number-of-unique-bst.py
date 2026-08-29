N = int(input())

# Please write your code here.
memo = [-1 for _ in range(N+1)]

def dp(n):
    if memo[n] != -1:
        return memo[n]
    if n == 0:
        memo[n] = 1
    elif n <= 2:
        memo[n] = n
    else:
        s = 0
        for i in range(n):
            s += dp(i)*dp(n-i-1)
        memo[n] = s
    return memo[n]

print(dp(N))
