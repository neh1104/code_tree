n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.

for j in range(x1[0], x2[0]+1):
    ch = 1
    for a, b in zip(x1[1:], x2[1:]):
        if a<=j<=b:
            continue
        ch = 0
        break
    if ch:
        print('Yes')
        break
if not(ch):
    print('No')