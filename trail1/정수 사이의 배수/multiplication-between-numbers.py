a, b = map(int, input().split())
cnt = 0
sum = 0
for i in range(a, b+1):
    if i % 5 == 0:
        sum += i
        cnt += 1
    elif i % 7 == 0:
        sum += i
        cnt += 1
print(sum, round(sum / cnt, 1))