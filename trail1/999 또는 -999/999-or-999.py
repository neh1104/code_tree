arr = list(map(int, input().split()))

max = arr[0]
min = arr[0]
for i in arr:
    if abs(i) == 999:
        break
    if i > max:
        max = i
    if i < min:
        min = i
print(max, min)