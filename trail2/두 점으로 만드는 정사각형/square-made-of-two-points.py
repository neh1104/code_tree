x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.


x = max(x1, x2, a1, a2) - min(x1, x2, a1, a2)
y = max(y1, y2, b1, b2) - min(y1, y2, b1, b2)

print(x*x if x > y else y*y)