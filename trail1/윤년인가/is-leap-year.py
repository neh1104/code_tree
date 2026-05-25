y = int(input())

if (y % 100 == 0 and y % 400 != 0) or y % 4 != 0:
    print('false')
else:
    print('true')