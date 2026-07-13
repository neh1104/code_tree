n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
segments.sort(key = lambda x: -x[1])
bs = segments[::]
b = segments[0][1] - segments[1][1]

segments.sort(key = lambda x: x[0])
aseg = segments[::]
a = segments[1][0] - segments[0][0]


if a > b:
    ls = aseg[1:]
else:
    ls = bs[1:]
    
a = 100; b = 0
for i in ls:
    if i[0] < a:
        a = i[0]
    if i[1] > b:
        b = i[1]
print(b-a)