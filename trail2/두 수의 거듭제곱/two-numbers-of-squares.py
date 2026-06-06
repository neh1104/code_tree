a, b = map(int, input().split())

# Please write your code here.

def ab(a, b):
    prod = 1
    for _ in range(b):
        prod *= a
    return prod

print(ab(a, b))