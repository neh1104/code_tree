a = list(map(int, input().split()))

mx = 0; mn = 1000
for i in a:
    if i > 500 and i < mn:
        mn = i
    if i < 500 and i > mx:
        mx = i
print(mx, mn)