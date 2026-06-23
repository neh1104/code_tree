N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
ls = [0]*1003
for a, b in ranges:
    for i in range(0, 1003):
        if i < a+1:
            ls[i]+=C
        elif i<=b+1:
            ls[i]+=G
        else:
            ls[i]+=H
#print(ls)
print(max(ls))