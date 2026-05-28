a, b = map(int, input().split())

cc = False
for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        cc = True
        break
print(1 if cc == 1 else 0)