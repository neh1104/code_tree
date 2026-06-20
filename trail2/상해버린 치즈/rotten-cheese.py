N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# Please write your code here.
ls = [[] for _ in range(N)]
cnt = 1

for i in range(S):
    #print('------')
    for j in range(D):
        #print(cnt)
        #cnt += 1
        if p[j] == sick_p[i] and t[j] < sick_t[i]:
            ls[p[j]-1].append(m[j])
        #else:
            #print(m[j],'okay')

ls = [ls[i] for i in range(N) if i + 1 in sick_p]
danger = []
if len(ls) > 1:
    for i in ls[0]:
        ch = 1
        for j in ls[1:]:
            if not(i in j):
                ch = 0
                break
        if ch:
            danger.append(i)
else:
    danger = ls[0]

#print(danger)
checked = []
MAX = 0
for i in danger:
    cnt = 0
    for j in range(D):
        if i == m[j]:
            if p[j] in checked:
                continue
            else:
                checked.append(p[j])
                cnt +=1
    MAX = max(MAX, cnt)

print(MAX)