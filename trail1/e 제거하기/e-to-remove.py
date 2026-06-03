a = input()

for i in range(len(a)):
    if a[i] == 'e':
        print(a[:i]+a[i+1:])
        break