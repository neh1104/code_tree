n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

# Please write your code here.
ch =1
for i in range(n):
    a = x1[:i]+x1[i+1:]
    b = x2[:i]+x2[i+1:]
    print
    max1 = max(a)
    min2 = min(b)
    #print(max1, min2)
    if max1 <= min2:
        ch = 0
        print('Yes')
        break
if ch:
    print('No')