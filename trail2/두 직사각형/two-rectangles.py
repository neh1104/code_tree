x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.

if x1 <= a2 and x2 >= a1 and y1 <= b2 and y2 >= b1:
    print('overlapping')
else:
    print('nonoverlapping')