n = int(input())

cmt = 1
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(cmt, end = ' ')
        else:
            if j == 0:
                cmt_2 = cmt+n-1
            print(cmt_2 - j, end = ' ')
        cmt += 1
    print()