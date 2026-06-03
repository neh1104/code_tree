A = input()

# Please write your code here.

a = []
n = 0; cnt = 0
for i in A:
    if i != n:
        a.append(i)
        a.append(1)
    else:
        a[-1] += 1
    n = i
ln = 0
for i in a:
    ln += len(str(i))
print(ln)
print(*a,sep = '')