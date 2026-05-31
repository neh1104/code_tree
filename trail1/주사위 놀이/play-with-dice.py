ls = [0] * 6

arr = list(map(int, input().split()))

for i in arr:
    ls[i-1] += 1

for i in range(6):
    print(f"{i+1} - {ls[i]}")