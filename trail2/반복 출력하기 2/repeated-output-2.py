n = int(input())

# Please write your code here.

def wornl(n):
    if n == 0:
        return
    print('HelloWorld')
    wornl(n-1)

wornl(n)