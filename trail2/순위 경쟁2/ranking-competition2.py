n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.

dir = {'A' : 0,
        'B' : 0}
ch = 'AB'
cnt = 0
for i in range(n):
    dir[c[i]] += s[i]
    if dir['A'] > dir['B'] and ch != 'A':
        cnt += 1
        ch = 'A'
    if dir['A'] < dir['B'] and ch != 'B':
        cnt += 1
        ch = 'B'
    if dir['A'] == dir['B'] and ch != 'AB':
        cnt += 1
        ch = 'AB'
print(cnt)