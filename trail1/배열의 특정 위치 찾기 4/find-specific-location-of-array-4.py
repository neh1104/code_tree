arr = list(map(int, input().split()))

ls = []

for i in arr:
    if i == 0:
        break
    ls.append(i)
_ls = []
for i in ls:
    if i % 2 == 0:
        _ls.append(i)

print(len(_ls), sum(_ls))