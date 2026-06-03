a = input()

q = input()

for i in range(len(q)):
    if q[i] == 'L':
        a = a[1:]+a[0]
    else:
        a = a[-1]+a[:-1]

print(a)