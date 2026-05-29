a, b, c = map(int, input().split())

ch = False

for i in range(a, b+1):
    if i % c == 0:
        ch = True
        break

print('YES' if ch == False else 'NO')