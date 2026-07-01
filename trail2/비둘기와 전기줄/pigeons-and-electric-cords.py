N = int(input())
pigeon = []
position = []
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

# Please write your code here.

ls = [2]*11
cnt = 0
for p, pos in zip(pigeon, position):
    if pos == 1 and ls[p] == 0:
        cnt += 1
    elif pos == 0 and ls[p] == 1:
        cnt += 1
    ls[p] = pos
print(cnt)