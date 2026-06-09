n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

class Where():
    def __init__(self, idx, x):
        self.idx, self.x = idx, x

where = [Where(i, sequence[i]) for i in range(n)]

where.sort(key = lambda x: (x.x, x.idx))

ls = []
for i in range(n):
    ls.append((where[i].idx, i+1))

ls.sort(key = lambda x: x[0])

for i in ls:
    print(i[1], end = ' ')