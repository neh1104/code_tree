n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]
x = 0
for i in arr:
        #it doesn't work effectly! Just use sum(i), do ot calculate one by one
    if sum(i) / 4 >= 60:
        x += 1
        print('pass')
    else:
        print('fail')
print(x)