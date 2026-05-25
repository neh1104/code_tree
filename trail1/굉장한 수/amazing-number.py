a = int(input())

if (a % 3 == 0 and a % 2 != 0) or (a % 2 == 0 and a % 5 == 0):
    print('true')
else:
    print('false')