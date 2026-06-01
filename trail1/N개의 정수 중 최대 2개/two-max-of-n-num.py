n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

max_id = 0

for i in range(n):
    if arr[i] > arr[max_id]:
        max_id = i

sec = min(arr)

for i in list(arr[:max_id]+arr[max_id+1:]):
    if i > sec:
        sec = i

print(arr[max_id], sec)
        