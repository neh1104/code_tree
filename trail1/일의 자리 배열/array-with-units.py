pp, p = map(int, input().split())
print(pp%10, p%10, end = ' ')
for _ in range(8):
    pp, p = p, pp + p
    print(p%10, end = ' ')