n = int(input())

arr = []
arr.append(1); arr.append(n)

i = 2
while True:
    arr.append(arr[i-1] + arr[i-2]) 
    if arr[i] > 100:
        break
    i += 1   

print(*arr)