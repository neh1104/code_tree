n = int(input())
c, s = [], []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.

def prize(a, b, c):
    ls = [0, 0, 0]
    if a >= b and a >= c:
        ls[0] = 1
    if b >= a and b >= c:
        ls[1] = 1
    if c >= a and c >= b:
        ls[2] = 1
    return ls

A, B, C = 0, 0, 0
ls = [0, 0, 0]
cnt = 0
for i in range(n):
    if s[i] == 0:
        continue
    if c[i] == 'A':
        A += s[i]
    if c[i] == 'B':
        B += s[i]
    if c[i] == 'C':
        C += s[i]
    n_ls = prize(A, B, C)
    if ls != n_ls:
        cnt += 1
        ls = n_ls

print(cnt)