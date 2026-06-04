n, a = input().split()
n = int(n)

cnt = 0
for _ in range(n):
    if input() == a:
        cnt += 1
print(cnt)