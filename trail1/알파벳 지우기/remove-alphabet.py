a = input()
b = input()

s = ['','']
k = 0
for i in [a, b]:
    for j in i:
        if j.isdigit():
            s[k] += j
    k += 1

print(int(s[0]) + int(s[1]))