a = list(input())

def switch():
    a.insert(0, a.pop(-1))

def check():
    n_cnt = 1
    n = a[0]
    ls = [n, n_cnt]
    for i in a:
        if i != n:
            n = i
            n_cnt = 1
            ls.append(i)
            ls.append(n_cnt)
        else:
            n_cnt += 1
            ls[-1] = n_cnt
        
    return ls

MIN = 30
for _ in range(len(a)):
    switch()
    LS = check()
    A = "".join(map(str, LS))
    MIN = min(len(A), MIN)
print(MIN)