n = int(input())

arr = [int(input()) for _ in range(n)]

sum_3 = 0
for i in arr:
    if i % 2 == 1 and i % 3 == 0:
        sum_3 += i
print(sum_3)