a = input()

# Please write your code here.
ch = False
ls = []
for i in a:
    if ch == False and i == '0':
        i = '1'
        ch = True
    ls.append(i)
    
if ch == False:
    ls[-1] = '0'

#print(ls)
sum = 0
for i in ls:
    sum = sum*2 + int(i)

print(sum)