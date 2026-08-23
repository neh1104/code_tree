n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
edges.sort(key = lambda x : x[1])

key = [0]
for k in range(1, n+1): 
    key_n = k
    for i, j in edges:
        if i == key_n:
            key_n = i+1
        elif i == key_n - 1:
            key_n = i
    key.append(key_n)

def where():
    for k in range(1, n+1): 
        key_n = k
        for i, j in ls:
            if i == key_n:
                key_n = i+1
            elif i == key_n - 1:
                key_n = i

        if key_n != key[k]:

            return 0
    return 1

MIN = m
ls = []
def ladder(curr):
    global MIN
    global ls

    if curr == m:
        if where():
            #print(ls)
            MIN = min(MIN, len(ls))
        return

    ls.append(edges[curr])
    ladder(curr+1)
    ls.pop()

    ladder(curr+1)


ladder(0)
print(MIN)
    