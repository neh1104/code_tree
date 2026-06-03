a = input()
n = int(input())
if n < len(a):
    a = a[::-1]
    for i in range(n):
        print(a[i],end = '')
else:
    print(a[::-1])