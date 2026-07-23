n = int(input())
a = list(map(int, input().split()))

def find_pivot(low, high):
    if high - low <= 2:
        return high

    mid = (low+high)//2
    if a[low] > a[high] and a[low] > a[mid]:
        if a[high] > a[mid]:
            return high
        else:
            return mid
    elif a[high] > a[low] and a[high] > a[mid]:
        if a[low] > a[mid]:
            return low
        else:
            return mid
    else:
        if a[high] > a[low]:
            return high
        else:
            return low

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def quick(a, low, high):
    if low < high:
        p_idx = find_pivot(low, high)
        swap(a, high, p_idx); p = a[high]

        #print(*a, ' ', p)
        p_idx = qsort(a, low, high, p)
        #print(*a, ' ', p_idx, '\n')
        quick(a, low, p_idx-1)
        quick(a, p_idx+1, high)

def qsort(a, low, high, p):
    j = low-1
    for i in range(low, high):
        if a[i] < p:
            j += 1
            swap(a, j, i)
    swap(a, j+1, high)

    return j+1

quick(a, 0, n-1)
print(*a)