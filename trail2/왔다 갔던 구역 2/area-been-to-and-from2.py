n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

ls = [0]*1000

s_p = 0
for i, d in zip(x, dir):
    if d == 'R':
        for j in range(s_p, s_p+i):
            ls[j] += 1
        s_p += i
    else:
        for j in range(s_p-1, s_p-i-1, -1):
            ls[j] += 1
        s_p -= i
#print(ls)
#print([x for x in ls if x >= 2])
print(len([x for x in ls if x >= 2]))