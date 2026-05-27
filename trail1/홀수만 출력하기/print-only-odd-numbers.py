n = int(input())
arr = [int(input()) for _ in range(n)]

for i in arr:
    if i % 3 == 0 and i % 2 == 1:
        print(i)
