arr = [int(input()) for _ in range(10)]

cnt = 0
sum = 0
for i in arr:
    if 0 <= i <=200:
        sum += i
        cnt += 1
print(sum, round(sum/cnt, 1))