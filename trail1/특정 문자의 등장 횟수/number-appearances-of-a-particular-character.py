a = input()

ee = 0; eb = 0 
for i in range(len(a)-1):
    if a[i]+a[i+1] == 'ee':
        ee += 1
    if a[i]+a[i+1] == 'eb':
        eb += 1

print(ee, eb)