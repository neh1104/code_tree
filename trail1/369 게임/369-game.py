n = int(input())

for i in range(1, n+1):
    if set(str(i)) & set('369') or i % 3 == 0: #there are more CLEAN statement!
        print(0, end = ' ')
    else:
        print(i, end = ' ')