arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        print(arr[i-1]+arr[i-2]+arr[i-3])
        break