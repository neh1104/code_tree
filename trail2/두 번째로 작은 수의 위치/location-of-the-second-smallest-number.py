n = int(input())
a = [0] + list(map(int, input().split()))

# Please write your code here.
min = [100, -1, 0]
last = [100, -1, 0]
for i in range(1, n+1):
    if a[i] < min[0]:
        last = min
        min = [a[i], i, 0]
    elif a[i] == last[0]:
        last[-1] += 1
    elif a[i] == min[0]:
        min[-1] += 1
    elif a[i] < last[0]:
        last = [a[i], i, 0]

#print(last)
if last[-1] > 0:
    print(-1)
else:
    print(last[-2])