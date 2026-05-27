a, b = map(int, input().split())
prod = 1
for _ in range(b):
    prod *= a
print(prod)