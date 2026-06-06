a, b = map(int, input().split())

# Please write your code here.

def bias(a, b):
    return (a+10, b*2) if a < b else (a*2, b+10)

a, b = bias(a, b)

print(a, b)