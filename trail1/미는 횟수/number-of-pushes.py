a = input()
b = input()

l_a = len(a)

ck = True
for i in range(l_a):
    a = a[-1] + a[:-1]
    if a == b:
        print(i+1)
        ck = False
        break

if ck:
    print(-1)