arr = list(map(int, input().split()))
ls_c = [0]*10

for i in arr:
    if i == 0:
        break
    ten = i//10
    ls_c[ten] += 1

for i in range(1,10):
    print(f'{i} - {ls_c[i]}')