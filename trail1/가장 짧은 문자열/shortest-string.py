mx = 0
mn = 20
for _ in range(3):
    ln = len(input())
    if ln > mx:
        mx = ln
    if ln < mn:
        mn = ln

print(mx - mn)