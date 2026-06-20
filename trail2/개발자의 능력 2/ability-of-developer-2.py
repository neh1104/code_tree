a = list(map(int, input().split()))

# Please write your code here.
S = sum(a)
n = 6

MIN = 1000000
for i in range(n-1):
    for j in range(i+1, n):
        for i2 in range(n-1):
            for j2 in range(i2+1, n-1):
                if i == i2 or j == j2 or i == j2 or j == i2:
                    continue
                #print(i, j, i2, j2)
                s1 = a[i]+a[j]
                s2 = a[i2]+a[j2]
                s3 = S-s1-s2

                cha = max(s1, s2, s3) - min(s1, s2, s3)
                MIN = min(MIN, cha)

print(MIN)