N = int(input())

# Please write your code here.

def wornl(n):
    if n == 1:
        return 1
    
    return wornl(n-1) + n

print(wornl(N))