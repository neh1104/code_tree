n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def re_2(arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] //= 2

re_2(arr)
print(*arr)