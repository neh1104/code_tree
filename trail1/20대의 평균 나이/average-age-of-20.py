cnt = 0
sum = 0
while True:
    c = int(input())
    if 20 <= c <= 29:
        sum += c
        cnt += 1
        continue
    print(f"{sum/cnt:.2f}")
    break
    