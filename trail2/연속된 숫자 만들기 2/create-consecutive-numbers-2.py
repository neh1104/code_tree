pos = list(map(int, input().split()))

# Please write your code here.

pos.sort()
a, b, c = pos

gap1 = b - a
gap2 = c - b

if gap1 == 1 and gap2 == 1:
    print(0)

elif gap1 == 2 or gap2 == 2:
    print(1)

else:
    print(2)