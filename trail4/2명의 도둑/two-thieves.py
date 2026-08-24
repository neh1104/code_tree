n, m, c = map(int, input().split())
w = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

ls = []; s = 0 
MAX = 0
def find_c(curr):
    global s
    global ls
    global MAX
    if s > c:
        return
    
    if curr == m:
        if s <= c:
            MAX = max(sum(list(i**2 for i in ls)), MAX)
        return

    find_c(curr+1)

    ls.append(now_ls[curr]); s += now_ls[curr]
    find_c(curr+1)
    ls.pop(); s -= now_ls[curr]

a_MAX = 0; b_MAX = 0
mapping = [[-1 for _ in range(n)] for _ in range(n)]
for ai in range(n):
    for aj in range(n-m+1):
        if mapping[ai][aj] == -1:
            now_ls = w[ai][aj:aj+m]
            MAX = 0
            find_c(0)
            mapping[ai][aj] = MAX
        a = mapping[ai][aj]

        for bi in range(n):
            for bj in range(n-m+1):
                if ai == bi and aj+m > bj:
                    continue
                if mapping[bi][bj] == -1:
                    now_ls = w[bi][bj:bj+m]
                    MAX = 0
                    find_c(0)
                    mapping[bi][bj] = MAX
                b = mapping[bi][bj]
                
                if a + b > a_MAX+b_MAX:
                    a_MAX = a; b_MAX = b
                    #print(ai, aj, '|', bi, bj, '|', a, b)

print(a_MAX+b_MAX)
