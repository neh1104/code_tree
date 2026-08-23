n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.
x = []
for i in range(n):
    x.append((x1[i], x2[i]))

x.sort(key = lambda x: (x[0], x[1]))

ls = []
MAX = 0
def wornl(curr):
    global ls
    global MAX
    if curr == n:
        if len(ls) >= 2 and ls[-2][1] >= ls[-1][0]:
            MAX = max(MAX, len(ls)-1)
        else:
            MAX = max(MAX, len(ls))
        return
    if len(ls) >= 2 and ls[-2][1] >= ls[-1][0]:
        MAX = max(MAX, len(ls)-1)
        return

    for i in [1, 0]:
        if i:
            ls.append((x[curr][0], x[curr][1]))  
        wornl(curr + 1)
        if i:
            ls.pop()
wornl(0)
print(MAX)