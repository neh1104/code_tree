n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
#print(arr, 'arr')
MAX = 0
for i in range(1, n+1):
    cnt = 0
    sum = 0
    ls = arr[::]
    while cnt < m:    
        sum += ls[i]
        i = ls[i]
        cnt += 1        
    MAX = max(MAX, sum)
        
print(MAX)