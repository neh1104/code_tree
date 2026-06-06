n = int(input())

# Please write your code here.

def wornl(n):
    if n == 0:
        return
    
    print('* '*n)
    wornl(n-1)
    print('* '*n)

wornl(n)