n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
MIN = 1000
for i in range(max(arr), max(arr[0], arr[-1])-1, -1):
    ls = []
    for idx, x in enumerate(arr):
        if x <= i:
            ls.append(idx)

    ch = 1
    for j in range(len(ls)-1):
        if ls[j+1] - ls[j] > k:
            ch = 0
            break
    if ch:
        MIN = min(MIN, i)

print(MIN)