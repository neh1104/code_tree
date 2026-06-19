ab = list(map(int, input().split()))

# Please write your code here.
import sys
sab = sum(ab)
MIN = sys.maxsize

for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            s = abs(abs(sab - ab[i]-ab[j]-ab[k])- ab[i]-ab[j]-ab[k])
            MIN = min(MIN, s)

print(MIN)