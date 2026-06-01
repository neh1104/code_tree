arr = list(map(int, input().split()))

max = arr[0]

for i in arr[1:]:
    if i > max:
        max = i

print(max)