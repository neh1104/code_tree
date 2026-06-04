a, b = input().split()

A = ''; B = ''

for i in a:
    if not(i.isdigit()):
        break
    A += i

for i in b:
    if not(i.isdigit()):
        break
    B += i

print(int(A) + int(B))