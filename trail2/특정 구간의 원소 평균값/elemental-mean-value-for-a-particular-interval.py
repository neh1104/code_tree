n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(n):
    for j in range(1, n-i+1):
        s = sum(arr[i:i+j])/j
        if s in arr[i:i+j]:
            #print(arr[i:i+j])
            cnt += 1
print(cnt)