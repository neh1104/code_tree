n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.

str.sort()
ls = []
for i in str:
    ch = True
    for j in range(len(t)):
        if t[j] != i[j]:
            ch = False
            break
        if len(i) < len(t):
            ch = False
            break
    if ch:
        ls.append(i)

print(ls[k-1])