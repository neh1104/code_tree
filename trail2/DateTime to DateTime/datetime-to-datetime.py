a, b, c = map(int, input().split())

# Please write your code here.

def f(a, b, c):
    if a < 11:
        return -1
    elif a == 11:
        if b < 11:
            return -1
        elif b == 11:
            if c < 11:
                return -1
    
    tt = (a-11)*24*60 + (b-11)*60 + c-11

    return tt

print(f(a, b, c))    