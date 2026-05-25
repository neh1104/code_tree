a, b, c = map(int, input().split())

if a > b > c or c > b > a:
    print(b)
elif (b > a and a > c) or (b < a and a < c):
    print(a)
else:
    print(c)