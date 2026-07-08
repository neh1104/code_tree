n = int(input())
arr = list(input().split())

# Please write your code here.
cnt = 0
A = ord('A')
for i in range(n):
    n = arr.index(chr(A+i))
    while n != i:
        if n > i:
            tmp = arr[n]
            arr[n] = arr[n-1]
            arr[n-1] = tmp
            n -= 1
        else:
            tmp = arr[n]
            arr[n] = arr[n+1]
            arr[n+1] = tmp
            n += 1
        cnt += 1

print(cnt)