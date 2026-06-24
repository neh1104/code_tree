n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
ls = [0]*101
for i in range(n):
    for j in range(i + 1, n):
        k = (a[i]+a[j])/2
        
        if k % 1 == 0:
            #print(k)
            ls[int(k)] += 1
#print(ls)
print(max(ls))