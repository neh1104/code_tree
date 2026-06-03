a = input()
A = len(a)
for i in range(A+1):
    if i == 0:
        print(a)
        continue
    print(a[-i:]+a[:A-i])
