n, t = map(int, input().split())
start = []
speed = []

for _ in range(n):
    s, v = map(int, input().split())
    start.append(s)
    speed.append(v)

# Please write your code here.
runners = sorted(zip(start, speed))

group_count = 1
last_pos = runners[-1][0] + runners[-1][1] * t

for i in range(n - 2, -1, -1):
    s, v = runners[i]
    reach_pos = s + v * t

    if reach_pos < last_pos:
        group_count += 1
        last_pos = reach_pos

print(group_count)