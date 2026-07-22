n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    min = i
    for j in range(i, n):
        if a[j] < a[min]:
            min = j
    
    if min != i:
        tmp = a[min]
        a[min] = a[i]
        a[i] = tmp

print(*a)