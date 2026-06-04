n = int(input())

s = 0
for _ in range(n):
    s += int(input())
s = str(s)
print(s[1:] + s[0])