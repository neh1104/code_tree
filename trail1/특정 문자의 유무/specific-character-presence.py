a = input()

ee = False; ab = False
for i in range(len(a)-1):
    if a[i]+a[i+1] == 'ee':
        ee = True
    if a[i]+a[i+1] == 'ab':
        ab = True

print('Yes' if ee == True else 'No', end = ' ')
print('Yes' if ab == True else 'No')