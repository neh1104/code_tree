n, t = map(int, input().split())
start = []
speed = []

for _ in range(n):
    s, v = map(int, input().split())
    start.append(s)
    speed.append(v)

# Please write your code here.

from sortedcontainers import SortedSet

runners = SortedSet()
for i in range(n):
    runners.add((start[i], start[i]+t*speed[i]))

#print(*runners)

cnt = 0; last = float('inf')
for i in range(n-1, -1, -1):
    st, end = runners[i] 
    if end < last:
        cnt += 1
        last = end
print(cnt)