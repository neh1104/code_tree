a = list(input())

ft = a[0]; sd = a[1]

new = ''
for i in a:
    if i == sd:
        new += ft
    else:
        new += i
print(new)