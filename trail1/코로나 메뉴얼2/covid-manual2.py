arr = [list(input().split()) for _ in range(3)]
ls = [0]*4
#print(arr)
for i in arr:
    cv_c = i[0]; cv_t = int(i[1])
    if cv_c == 'Y':
        if cv_t >= 37:
            ls[0] += 1
        else:
            ls[2] += 1
    else:  
        if cv_t >= 37:
            ls[1] += 1
        else:
            ls[3] += 1
print(*ls, 'E' if ls[0]>=2 else '')