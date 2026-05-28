ls = []
while True:
    n = int(input())
    
    if n == 0:
        break
    ls.append(n)

print(*ls, sep = '\n')