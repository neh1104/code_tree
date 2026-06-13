n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

dx = {'W': -1, 'S': 0, 'N': 0, 'E': 1}
dy = {'W': 0, 'S': -1, 'N': 1, 'E': 0}

def move(d, i, arr):
    arr[0], arr[1] = arr[0] + dx[d]*i, arr[1] + dy[d]*i
    return arr

ls = [0, 0]
for i, d in zip(dist, dir):
    ls = move(d, i, ls)

print(*ls)