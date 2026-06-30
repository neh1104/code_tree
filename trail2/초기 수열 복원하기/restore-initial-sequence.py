n = int(input())
ad = list(map(int, input().split()))

# Please write your code here.

for i in range(1, n+1):
    ls = [i]
    for j in range(1, n):
        x = ad[j-1]-ls[-1]
        if x in ls or not(1<=x<=n):
            break
        ls.append(x)
    if len(ls) == n:
        print(*ls)
        break