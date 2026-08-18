n, m, r, c = map(int, input().split())
directions = list(input().split())

# Please write your code here.
def in_range(x, y):
    return 0<=x<n and 0<=y<n

a = [[0 for _ in range(n)] for _ in range(n)]
r -= 1; c -= 1
a[r][c] = 6

ls = [1, 2, 3, 6, 5, 4]
#(0, 3), (1, 4), (2, 5) 가 각각 세트

for d in directions:
    if d == 'L':
        if in_range(r, c-1):
            c -= 1
            ls[0], ls[2], ls[3], ls[5] = ls[2], ls[3], ls[5], ls[0]
    if d == 'R':
        if in_range(r, c+1):
            c += 1
            ls[0], ls[2], ls[3], ls[5] = ls[5], ls[0], ls[2], ls[3]
    if d == 'U':
        if in_range(r-1, c):
            r -= 1
            ls[0], ls[1], ls[3], ls[4] = ls[1], ls[3], ls[4], ls[0]
    if d == 'D':
        if in_range(r+1, c):
            r += 1
            ls[0], ls[1], ls[3], ls[4] = ls[4], ls[0], ls[1], ls[3]

    a[r][c] = ls[3]

s = 0
for i in a:
    s += sum(i)

print(s)