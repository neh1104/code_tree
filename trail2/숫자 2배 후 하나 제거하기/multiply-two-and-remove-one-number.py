n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
MIN = 100*100
for i in range(n):
    arr[i] *= 2
    
    for j in range(n):
        if i == j:
            continue
        ls = []
        for k in range(n):
            if k == j:
                continue
            ls.append(arr[k])
        sum = 0
#        print(ls)
        for t in range(n-2):
            sum += abs(ls[t+1]-ls[t])
        MIN = min(MIN, sum)
    arr[i]//=2

print(MIN)