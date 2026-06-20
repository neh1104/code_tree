

n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
def check(m, a):
    cnt1 = 0
    cnt2 = 0
    if str(ls[m]) == a[m]:
        cnt1 += 1
    elif str(ls[m]) in a:
        cnt2 += 1
    return cnt1, cnt2

LS = [[] for _ in range(n)]

for i in range(1, 10):
    for j in range(1, 10):
        if j == i:
            continue
        for k in range(1, 10):
            if k == i or k == j:
                continue
            ls = [i, j, k]

            for N in range(n): # n개의 숫자들에 대해 확인
                cnt1 = 0
                cnt2 = 0
                for M in range(3): # 세자리 확인
                    cnt = check(M, str(a[N]))
                    cnt1 += cnt[0]
                    cnt2 += cnt[1]

                if cnt1 != b[N] or cnt2 != c[N]:
                    break
                else:
                    LS[N].append(100*i+10*j+k)

cnt = 0
for i in LS[0]:
    ch = 1
    for j in LS[1:]:
        if not(i in j):
            ch = 0
            break
    if ch:
        cnt += 1


print(cnt)