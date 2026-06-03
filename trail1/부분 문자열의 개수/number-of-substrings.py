a = input()
b = input()

ln_a = len(a); ln_b = len(b)
cnt = 0
for i in range(ln_a - ln_b + 1):
    isit = True
    for j in range(ln_b):
        if a[i+j] != b[j]:
            isit = False
            break
    if isit == True:
        cnt += 1

print(cnt)