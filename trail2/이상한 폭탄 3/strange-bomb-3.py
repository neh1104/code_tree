N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

def bomb(j):
    st = j-K if j-K > 0 else 0
    end = j+K+1 if j+K+1<=N else N
    for i in range(st, end):
        if i == j:
            continue
        if num[j] == num[i]:
            return 1
    return 0

ls = []
bls = []
for i in range(N):
    if num[i] in ls:
        continue
    ls.append(num[i])
    cnt = 0
    for j in range(N):
        if num[i] == num[j]:
            cnt += bomb(j)
    bls.append((cnt, num[i]))

#print(bls)
bls.sort(key = lambda x: (-x[0], -x[1]))
print(bls[0][1] if bls[0][0] != 0 else 0)