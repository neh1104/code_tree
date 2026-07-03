a, b, x, y = map(int, input().split())

# Please write your code here.

len1 = abs(a-b)

len2 = abs(a-x) + abs(b-y)

len3 = abs(a-y) + abs(b-x)

print(min(len1, len2, len3))