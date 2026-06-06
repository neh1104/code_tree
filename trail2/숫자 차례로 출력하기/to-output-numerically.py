n = int(input())

# Please write your code here.

def wornl1(n):
    if n == 0:
        return
    wornl1(n-1)
    print(n, end = ' ')

def wornl2(n):
    if n == 0:
        return
    print(n, end = ' ')
    wornl2(n-1)

wornl1(n)
print()
wornl2(n)