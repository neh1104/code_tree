n = int(input())
a = list(map(int, input().split()))

def mm(a, low, high):
    if low < high:
        mid = (low+high)//2
        mm(a, low, mid)
        mm(a, mid+1, high)
        merge(a, low, mid, high)
        #print(*a)


def merge(a, low, mid, high):
    sorting_a = []
    i = low; j = mid+1
    k = 0
    while i <= mid and j <= high:
        if a[i] < a[j]:
            sorting_a.append(a[i])
            i += 1; k += 1
        else:
            sorting_a.append(a[j])
            j += 1; k += 1
        
    if i <= mid:
        while i <= mid:
            sorting_a.append(a[i])
            i += 1; k += 1
    else:
        while j <= high:
            sorting_a.append(a[j])
            j += 1; k += 1
    
    for x in range(k):
        a[low+x] = sorting_a[x]


mm(a, 0, n-1)
print(*a)