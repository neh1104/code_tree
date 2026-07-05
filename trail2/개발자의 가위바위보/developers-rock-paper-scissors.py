N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)

# Please write your code here.
ls = []
for i in range(N):
    if a[i] != b[i]:
        ls.append((a[i]-b[i]+3)%3)

print(max(ls.count(1), ls.count(2)))