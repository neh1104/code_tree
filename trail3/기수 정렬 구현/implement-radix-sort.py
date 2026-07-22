n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for k in range(6):
    a = [[]for _ in range(10)]
    for i in range(n):
        point_num = (arr[i]%(10**(k+1)))//(10**(k))
        a[point_num].append(arr[i])
   
    sorted_ls = []
    for i in range(10):
        for j in range(len(a[i])):
            sorted_ls.append(a[i][j])

    arr = sorted_ls

print(*arr)