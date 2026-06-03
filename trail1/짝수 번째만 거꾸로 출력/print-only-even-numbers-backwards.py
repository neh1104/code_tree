a = input()

a = a[::-1]
print(a[::2] if len(a) % 2 == 0 else a[1::2])