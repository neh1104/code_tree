cnt = 0; s = []
while True:
    a = input()
    if a != '0':
        if cnt % 2 == 0:
            s.append(a)
    else:
        break
    cnt += 1
print(cnt)
print(*s, sep = '\n')