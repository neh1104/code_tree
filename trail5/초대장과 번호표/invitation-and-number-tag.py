N, G = map(int, input().split())

group = []
group_size = []

for _ in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(nums[1:])

# Please write your code here.

from collections import deque

gs_ls = [i for i in group_size]
n_ls = [[] for _ in range(N+1)]
dq = deque([1])
vt = [0 for _ in range(N+1)]
vt[1] = 1
cnt = 1

for i in range(G):
    for n in group[i]:
        n_ls[n].append(i)

while dq:
    #print()
    n = dq.pop()
    #print(n)
    for i in n_ls[n]:
        gs_ls[i] -= 1
        if gs_ls[i] == 1:
            #print(i)
            for j in group[i]:
                if vt[j]:
                    continue
                dq.append(j)
                vt[j] = 1
                cnt += 1
                #print(j, 'new', cnt)
#print()
print(cnt)