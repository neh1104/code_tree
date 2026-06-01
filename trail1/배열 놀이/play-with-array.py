n, q = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(q):
    i = input().split()
    #print(i)    
    fst = int(i[0])
    scd = int(i[1])
    last = int(i[-1])

    if fst == 1:
        print(arr[last-1])
    elif fst == 2:
        print(arr.index(last) + 1 if last in arr else 0)
    else:
        print(*arr[scd-1:last])