n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
n = max(pos)
ls = ['X']*n

for p, a in people:
    ls[int(p)-1] = a

#print(ls)
MAX = 0
for i in range(n):
    for j in range(i, n):
        if ls[i] in 'GH' and ls[j] in 'GH':
            if ls[i:j+1].count('G') == ls[i:j+1].count('H'):
                ln = j-i
                #print(ln, ls[i:j])
                #print(i, j)
                MAX = max(MAX, ln)
            elif not('H' in ls[i:j+1] and 'G' in ls[i:j+1]) or not('G' in ls[i:j+1] and 'H' in ls[i:j+1]):
                ln = j-i
                #print('only', i)
                #print(i, j)
                MAX = max(MAX, ln)

print(MAX)