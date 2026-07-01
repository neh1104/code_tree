x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.

if (x1 <= x4 and x2>=x3) or (x2 >= x3 and x2 <= x4):
    print('intersecting')
else:
    print('nonintersecting')