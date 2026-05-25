arr = [input().split() for i in range(3)]
ch = 0 

for i in arr: #증상유무 확인
    if i[0] == 'Y' and int(i[1]) >= 37:
        ch += 1

print('E' if ch >=2 else 'N')
    
