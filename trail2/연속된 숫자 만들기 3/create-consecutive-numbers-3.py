a = list(map(int, input().split()))

# Please write your code here.

a, b, c = a

ab = abs(a-b)
bc = abs(b-c)
print(max(ab, bc) - 1)