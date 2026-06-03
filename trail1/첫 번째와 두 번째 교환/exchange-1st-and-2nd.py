a = input()

fst = a[0]; snd = a[1]
new = ''
for i in a:
    if i == fst:
        new += snd
    elif i == snd:
        new += fst
    else:
        new += i
print(new)