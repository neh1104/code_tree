N, G = map(int, input().split())

group = []
group_size = []

for _ in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(nums[1:])

# Please write your code here.

from collections import deque

person_groups = [[] for _ in range(N + 1)]
for i in range(G):
    for person in group[i]:
        person_groups[person].append(i)

left_cnt = group_size.copy()
group_sets = [set(g) for g in group]

invited = [False] * (N + 1)
queue = deque()

invited[1] = True
queue.append(1)

while queue:
    curr = queue.popleft()
    
    for g_idx in person_groups[curr]:
        if curr in group_sets[g_idx]:
            group_sets[g_idx].remove(curr)
            left_cnt[g_idx] -= 1
            
            if left_cnt[g_idx] == 1:
                last_person = list(group_sets[g_idx])[0]
                if not invited[last_person]:
                    invited[last_person] = True
                    queue.append(last_person)

print(sum(invited))