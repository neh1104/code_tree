a, b, c = map(int, input().split())

cc = 0
for i in range(a, b+1):
    if i % c == 0:
        cc = 1
        break
print('YES' if cc == 1 else 'NO')