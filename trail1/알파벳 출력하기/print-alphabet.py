n = int(input())
ch = ord('A')

for i in range(n):
    for j in range(i+1):
        print(chr(ch), end = '')
        ch+=1
        if chr(ch-1) == 'Z':
            ch = ord('A')
    print()