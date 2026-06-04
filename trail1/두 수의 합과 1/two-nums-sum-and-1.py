a, b = map(int, input().split())

cnt = 0
for i in str(a+b):
    if i == '1':
        cnt += 1

print(cnt)