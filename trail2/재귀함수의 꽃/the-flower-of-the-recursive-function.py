N = int(input())

# Please write your code here.

def wornl(n):
    if n == 0:
        return
    print(n, end = ' ')
    wornl(n-1)
    print(n, end = ' ')

    
    
wornl(N)