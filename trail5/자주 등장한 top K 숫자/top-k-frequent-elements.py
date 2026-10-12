n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

dt = dict()

for i in arr:
    dt[i] = dt.get(i, 0) + 1

dt = sorted(dt.items(), key=lambda x : (x[1], x[0]), reverse = True)

for i in dt[:k]:
    print(i[0], end = ' ')