N = int(input())

# Please write your code here.
from collections import deque
vt = [0 for _ in range(N*2)]
def bfs():
    q = deque([N])
    while q:
        a = q.popleft()
        #print(a, vt[a])
        if a == 1:
            return vt[a]

        dist = vt[a]
        if a % 3 == 0:
            if vt[a//3] == 0:
                vt[a//3] = dist+1
                q.append(a//3)
        if a % 2 == 0:
            if vt[a//2] == 0:
                vt[a//2] = dist+1
                q.append(a//2)

        if vt[a+1] == 0:
            vt[a+1] = dist+1
            q.append(a+1)

        if vt[a-1] == 0:
            vt[a-1] = dist+1
            q.append(a-1)

print(bfs())