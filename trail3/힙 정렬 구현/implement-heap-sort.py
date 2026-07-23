n = int(input())
a = [0]+list(map(int, input().split()))

def heapify(a, n, i):
    lst = i; l = 2*i; r = 2*i + 1
    if l <= n and a[l] > a[lst]:
        lst = l
    if r <= n and a[r] > a[lst]:
        lst = r
    if lst != i:
        a[lst], a[i] = a[i], a[lst]
        heapify(a, n, lst)

def hsort(a, n):
    #make maxheap
    for i in range(n//2, 0, -1):
        heapify(a, n, i)
        #print(*a)
    #sorting
    for i in range(n):
        a[n-i], a[1] = a[1], a[n-i]
        heapify(a, n-i-1, 1)

hsort(a, n)
print(*a[1:])