a = int(input())

if a % 2 ==0:
    a /= 2
if a % 2 != 0:
    a += 1
    a /= 2
print(int(a))