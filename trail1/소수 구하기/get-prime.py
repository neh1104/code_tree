n = int(input())
cnt = 0
for i in range(2, n+1):
    n_ch = True
    for j in range(1, i):
        if i % j == 0 and j != 1:
            n_ch = False
            break
    if n_ch == True:
        print(i, end = ' ')



    