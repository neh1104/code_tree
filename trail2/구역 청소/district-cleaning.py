a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.

ls = [0]*101

def up(x, y):
    for i in range(x, y):
        ls[i] += 1

up(a, b)
up(c, d)

#print(ls)
cnt = 0
for i in ls:
    if i > 0:
        cnt += 1

print(cnt)