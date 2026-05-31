n = int(input())
arr = list(map(int, input().split()))
ls = [0] * 9

for i in arr:
    ls[i-1] += 1

print(*ls, sep = '\n')
