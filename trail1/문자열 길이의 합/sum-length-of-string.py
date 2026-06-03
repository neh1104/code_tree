n = int(input())

sum = 0
cnt = 0

for i in range(n):
    x = input()
    sum += len(x)
    if x[0] == 'a':
        cnt += 1

print(sum, cnt)