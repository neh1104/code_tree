arr = [list(map(int, input().split())) for _ in range(4)]

for i in range(4):
    print(sum(arr[i]))