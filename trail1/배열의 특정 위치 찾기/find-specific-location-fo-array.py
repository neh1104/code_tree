arr = list(map(int, input().split()))


print(sum(arr[1::2]), round(sum(arr[2::3])/len(arr[2::3]), 1))