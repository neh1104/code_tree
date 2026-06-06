n, m = map(int, input().split())

# Please write your code here.

def f(n, m):
    num = n if n < m else m

    for i in range(num,0, -1):
        if n % i == 0 and m % i == 0:
            print(i)
            break
    
f(n, m)