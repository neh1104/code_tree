n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
sum = 0
for i in range(n):
    sum1, sum2 = 0, 0
    I, J = a[i][0], a[0][i]
    ch1, ch2 = 1, 1
    for j in range(n):
        if a[i][j] == I:
            sum1 += 1
        else:
            sum1 = 1
            I = a[i][j] 
        if a[j][i] == J:
            sum2+=1
        else:
            sum2 = 1
            J = a[j][i]
       
        if ch1 and sum1 >= m:
            sum += 1
            ch1 = 0
        if ch2 and sum2 >= m:
            sum += 1
            ch2 = 0
print(sum)