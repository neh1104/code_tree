n = int(input())

cnt = 0
i = 1
while cnt < 2:
    if n*i % 5 == 0:
        cnt += 1
    print(n*i, end = ' ')
    i+=1
    