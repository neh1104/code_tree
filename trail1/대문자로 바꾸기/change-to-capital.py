arr = [list(input().split()) for _ in range(5)]

dif = ord('A') - ord('a')

for i in range(5):
    for j in range(3) :
        elm = arr[i][j]
        print(chr(ord(elm)+dif), end = ' ')
    print()