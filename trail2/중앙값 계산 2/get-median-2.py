n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def f(a, n):
    a.sort()
    print(a[n//2], end = ' ')

ls = []

for i in range(n):
    ls.append(arr[i])
    if i % 2 == 0:
        f(ls, i)
