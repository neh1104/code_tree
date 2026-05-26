a, b = map(int, input().split())
if a % 2 == 0:
    a += 1

for i in range(a, b + 1, 2):
    print(i, end = ' ')