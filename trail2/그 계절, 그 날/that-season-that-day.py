Y, M, D = map(int, input().split())

# Please write your code here.

def leaf(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    return False

def isit(y, m, d):
    if m == 2:
        if leaf(y):
            return 29
        return 28
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        return -1

def season(m):
    if 3<= m <= 5:
        return 'Spring'
    elif 6 <= m <= 8:
        return 'Summer'
    elif 9 <= m <= 11:
        return 'Fall'
    else:
        return 'Winter'


if 1 <= D <= isit(Y, M, D):
    print(season(M))
else:
    print(-1)