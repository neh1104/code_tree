a = list(input())


while True:
    if len(a) == 1:
        break
    n = int(input())
    if n < len(a):
        a.pop(n)
    else:
        a.pop(-1)
    print(*a, sep = '')
    