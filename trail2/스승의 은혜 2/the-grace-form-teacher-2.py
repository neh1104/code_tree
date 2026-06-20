n, B = map(int, input().split())
P = [int(input()) for _ in range(n)]

# Please write your code here.
P.sort()
#print(P)
MAX = 0
for i in range(n):
    b = B
    cnt = 0
    for j in range(n):
        if j == i and b >= P[j]//2:
            b -= P[j]//2
            cnt += 1
        elif b >= P[j]:
            b -= P[j]
            cnt += 1
        else:
            break
        MAX = max(MAX, cnt)

print(MAX)