n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]
ls = 0
for i in arr:
    x = 0
    for j in range(4):
        x += i[j]
    if x / 4 >= 60:
        ls += 1
        print('pass')
    else:
        print('fail')
print(ls)