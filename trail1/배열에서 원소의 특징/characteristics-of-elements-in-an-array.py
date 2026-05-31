arr = list(map(int, input().split()))

n = 0
for i in arr:
    if i % 3 == 0:
        print(n)
        break
    n = i