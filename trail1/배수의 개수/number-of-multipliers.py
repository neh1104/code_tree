arr = [int(input()) for _ in range(10)]

cnt3 = 0 
cnt5 = 0   
for i in arr:
    if i % 3 == 0:
        cnt3 += 1
    if i % 5 == 0:
        cnt5 += 1
print(cnt3, cnt5)