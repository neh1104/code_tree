n = int(input())

for i in range(n):
    for j in range(n):
        print(f"{i+1} * {j+1} = {(i+1)*(j+1)}", end = '')
        if j+1 < n:
            print(',', end = ' ')
    print()