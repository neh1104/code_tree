arr = list(map(int, input().split()))

# Please write your code here.
MIN = 1000
for i in range(4):
    for j in range(i+1, 5):
        for i2 in range(4):
            for j2 in range(i2+1, 5):
                if i in [i2, j2] or j in [i2, j2]:
                    continue
                
                s1 = arr[i] + arr[j]
                s2 = arr[i2] + arr[j2]
                s3 = sum(arr) - s1 - s2
                if s1 == s2 or s1 == s3 or s2 == s3:
                    continue
                MIN = min(MIN, max(s1, s2, s3)- min(s1, s2, s3))

print(MIN if MIN != 1000 else -1)