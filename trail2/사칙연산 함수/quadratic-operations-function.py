a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def plus(x, y):
    return x+y

def minus(x, y):
    return x - y

def multiple(x,y):
    return x * y

def dev(x, y):
    return x // y


if o == '+':
    print(f'{a} {o} {c} = ', end = '')
    print(plus(a, c))
elif o == '-':
    print(f'{a} {o} {c} = ', end = '')
    print(minus(a, c))
elif o == '*':
    print(f'{a} {o} {c} = ', end = '')
    print(multiple(a, c))
elif o == '/':
    print(f'{a} {o} {c} = ', end = '')
    print(dev(a, c))
else:
    print(False)