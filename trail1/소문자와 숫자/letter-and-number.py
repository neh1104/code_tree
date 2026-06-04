a = input()

len = ord('a') - ord('A')
s = ''
for i in a:
    if i.isdigit() == True:
        s += i
    if i.isalpha() == True:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            s += chr(ord(i)+len)
        else:
            s += i

print(s)