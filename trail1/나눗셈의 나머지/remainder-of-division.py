a, b = map(int, input().split())
ls = [0]*b

while True:
    x = a % b
    ls[x] += 1
    a = a // b    
    if a <= 1:
        break
print(sum(x**2 for x in ls))
# 18 9 0
# 9 4 1
# 4 2 0
# 2 1 0
#