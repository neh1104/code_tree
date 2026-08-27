n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


vt = [0 for i in range(n)]
MAX = 0
ls = []
def choose(curr, d):
    global MAX

    if curr == n:
        MAX = max(MAX, d)
        return

    for i in range(n):
        if vt[i]:
            continue

        vt[i] = 1; ls.append(A[curr][i])
        p = d if d < A[curr][i] else A[curr][i]
        choose(curr+1, p)
        vt[i] = 0; ls.pop()

choose(0, 10000)
print(MAX)