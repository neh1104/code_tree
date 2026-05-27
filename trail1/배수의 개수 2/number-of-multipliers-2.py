arr = [int(input()) for _ in range(10)]

cnt = 0
for i in arr:
    if i % 2 == 1:
        cnt += 1
print(cnt)