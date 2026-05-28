n = int(input())

cc = True
for i in range(2, n):
    if n % i == 0:
        cc = False
        break
print('C' if cc == False else 'N')