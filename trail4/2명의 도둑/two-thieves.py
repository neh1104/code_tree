n, m, c = map(int, input().split())
w = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

MAX = 0
def find_c(curr, s, ss):
    global MAX
    if s > c:
        return
    
    if curr == m:
        if s <= c:
            MAX = max(ss, MAX)
        return

    find_c(curr+1, s, ss)

    a = now_ls[curr]
    find_c(curr+1, s+a, ss+a**2)


a_MAX = 0; b_MAX = 0
mapping = [[-1 for _ in range(n)] for _ in range(n)]
for ai in range(n):
    for aj in range(n-m+1):
        if mapping[ai][aj] == -1:
            now_ls = w[ai][aj:aj+m]
            MAX = 0
            find_c(0, 0, 0)
            mapping[ai][aj] = MAX
        a = mapping[ai][aj]

        for bi in range(n):
            for bj in range(n-m+1):
                if ai == bi and aj+m > bj:
                    continue
                if mapping[bi][bj] == -1:
                    now_ls = w[bi][bj:bj+m]
                    MAX = 0
                    find_c(0, 0, 0)
                    mapping[bi][bj] = MAX
                b = mapping[bi][bj]
                
                if a + b > a_MAX+b_MAX:
                    a_MAX = a; b_MAX = b
                    #print(ai, aj, '|', bi, bj, '|', a, b)

print(a_MAX+b_MAX)
