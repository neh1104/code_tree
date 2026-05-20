arr = list(map(int, input().split()))
ls = []
for i in arr:
    if i == 0:
        break
    ls.append(i)

for i in ls[::-1]:
    print(i, end = ' ')