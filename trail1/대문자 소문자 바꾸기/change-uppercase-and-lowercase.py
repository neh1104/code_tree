a = input()

diff = ord('a') - ord("A")
s = ''
for i in a:
    I = ord(i)
    if I >= ord('A') and I <= ord('Z'):
        s += chr(I+diff)
    else:
        s += chr(I-diff)

print(s)