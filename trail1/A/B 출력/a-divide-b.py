a, b = map(int, input().split())

print(a // b, end = '.')
for _ in range(20):
    a = a % b *10
    print(a // b, end = '')