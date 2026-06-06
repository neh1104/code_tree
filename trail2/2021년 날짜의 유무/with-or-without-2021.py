M, D = map(int, input().split())

# Please write your code here.

def isit(m, d):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return d>=1 and d <=31
    elif m == 2:
        return d>=1 and d<= 28
    elif m in [4, 6, 9, 11]:
        return d>= 1 and d <= 30
    else:
        return False

print('Yes' if isit(M, D) else 'No')
