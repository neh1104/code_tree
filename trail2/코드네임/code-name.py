MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.

class Cas():
    def __init__(self, cd, sc):
        self.cd = cd
        self.sc = sc
cas = []
for i in range(MAX_N):
    cas.append(Cas(codenames[i], scores[i]))

min = [0, 100]
for i in range(MAX_N):
    if cas[i].sc <= min[1]:
        min = [cas[i].cd, cas[i].sc]
    
print(*min)
