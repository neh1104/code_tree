
n, m = map(int, input().split())
nums = list(map(int, input().split()))

from sortedcontainers import SortedSet

s = SortedSet([(0, n)])
l = SortedSet([(n+1, 1)])

for i in nums:
    x = s.bisect_right((i, n+1)) - 1
    a, b = s[x]
    s.remove((a, b))

    length = b - a + 1
    y = l.bisect_left((length, 0))
    cnt = l[y][1]

    l.remove((length, cnt))
    if cnt > 1:
        l.add((length, cnt - 1))

    if i - 1 >= a:
        s.add((a, i - 1))
        length = i - a
        y = l.bisect_left((length, 0))

        if y < len(l) and l[y][0] == length:
            cnt = l[y][1]
            l.remove((length, cnt))
            l.add((length, cnt + 1))
        else:
            l.add((length, 1))

    if i + 1 <= b:
        s.add((i + 1, b))
        length = b - i
        y = l.bisect_left((length, 0))

        if y < len(l) and l[y][0] == length:
            cnt = l[y][1]
            l.remove((length, cnt))
            l.add((length, cnt + 1))
        else:
            l.add((length, 1))

    print(l[-1][0] if l else 0)
