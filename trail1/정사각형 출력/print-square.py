n = int(input())

cnt = 1
while cnt <= n*n:
    print(cnt, end = ' ')
    if cnt % n == 0:
        print()
    cnt +=1