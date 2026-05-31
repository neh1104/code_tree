arr = list(map(int, input().split()))
ls = [0]*11

for i in arr:
    if i == 0:
        break
    t_s = i // 10
    ls[t_s] += 1

for i in range(10,0,-1):
    print(f'{i*10} - {ls[i]}')