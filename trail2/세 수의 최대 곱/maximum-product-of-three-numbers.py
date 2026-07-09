n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
i = arr[-1]*arr[-2]*arr[-3]
ii = arr[0]*arr[1]*arr[-1]
iii = 0 if arr.count(0) > 0 else i
iv, v = i, i
def in_range(N):
    return 0 <= N < n
lsiv = []; lsv = []
for a in range(n):
    if arr[a] >= 0:
        for j in range(3):
            if in_range(a-i-1):
                lsiv.append(arr[a-i-1])
            if in_range(a-i+1):
                lsv.append(arr[a-i+1])

if len(lsiv) == 3:
    iv = lsiv[0]*lsiv[1]*lsiv[2]

if len(lsv) == 3:
    v = lsv[0]*lsv[1]*lsv[2]

#print(max(i, ii, iii, iv, v))

i = arr[-1]*arr[-2]*arr[-3]
ii = arr[0]*arr[1]*arr[-1]
iii = 0 if arr.count(0) > 0 else i

print(max(i, ii, iii))