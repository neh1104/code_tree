a = input()
b = input()

c = ''
for i in [*a, *b]:
    if i != ' ':
        c = c + i
print(c)