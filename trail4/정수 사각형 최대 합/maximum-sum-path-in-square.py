n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
memo = [[0 for _ in range(n+1)] for _ in range(n+1)]

def dp(r, c):
    if memo[r][c] != 0:
        return memo[r][c] #
    
    if r == 0 and c == 0:
        memo[r][c] = grid[r][c]

    elif c == 0:
        memo[r][0] = dp(r-1, 0)+grid[r][c]
    elif r == 0:
        memo[0][c] = dp(0, c-1)+grid[r][c]
    else:
        memo[r][c] = max(dp(r, c-1), dp(r-1, c))+grid[r][c]
    
    return memo[r][c]

print(dp(n-1, n-1))