N = int(input())

# Please write your code here.
memo = [-1 for _ in range(N+1)]

def fibo(curr):
    if curr < 3:
        memo[curr] = 1
        
    if memo[curr] != -1:
        return memo[curr]

    memo[curr] = fibo(curr-2)+fibo(curr-1)
    return memo[curr]

print(fibo(N))