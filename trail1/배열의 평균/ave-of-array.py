arr = [list(map(int, input().split())) for _ in range(2)]

index = 0

for i in range(2):
    index = round(sum(arr[i]) / 4, 1) 
    print(index, end = ' ')

print()

for j in range(4):
    low = 0
    for i in range(2):
        low += arr[i][j]
    low = round(low/2, 1)
    print(low, end = ' ')

print()

avg = 0; cnt = 0
for i in range(2):
    for j in range(4):
        avg += arr[i][j]
        cnt += 1
avg = round(avg/cnt, 1)
print(avg)