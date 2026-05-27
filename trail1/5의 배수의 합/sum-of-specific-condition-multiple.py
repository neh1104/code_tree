a, b = map(int, input().split())

if a > b:
    cmd = b
    b = a
    a = cmd
sum = 0
for i in range(a, b+1):
    if i % 5 == 0:
        sum += i
print(sum)