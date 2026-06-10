a, b, c, d = map(int, input().split())

# Please write your code here.

def qusghks(h, m):
    h = h*60
    return h+m

ab = qusghks(a, b)
cd = qusghks(c, d)
print(cd - ab)