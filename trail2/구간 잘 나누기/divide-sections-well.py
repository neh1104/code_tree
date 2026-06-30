n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
st = max(a)
end = sum(a)

for M in range(st, end):
    sum = 0
    slice = 0
    for i in range(n):
        if sum+a[i] <= M:
            sum += a[i]
        else:
            sum = a[i]
            slice += 1
    if slice <= m-1:
        print(M)
        break
