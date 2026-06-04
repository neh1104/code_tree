a = input()

len =  ord('a') - ord('A')
s = ''
for i in a:
    I = ord(i)
    if I >= ord('a') and I <= ord('z'):
        s += chr(ord(i)-len)
    elif I >= ord('A') and I <= ord('Z'):
        s += i

print(s)