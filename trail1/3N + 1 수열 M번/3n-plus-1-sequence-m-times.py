m = int(input())
for _ in range(m):
    ct = 0
    n = int(input())
    while True:
        if n == 1:
            break
            
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3+1
        ct += 1

    print(ct)