T = int(input())

mapping = {
    'U': 0,
    'L': 1,
    'D': 2,
    'R': 3
}

# 좌표평면 기준
dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]


for _ in range(T):

    N = int(input())

    marbles = {}

    xs = []
    ys = []

    for number in range(1, N + 1):
        x, y, weight, direction = input().split()

        x = int(x) * 2
        y = int(y) * 2
        weight = int(weight)
        direction = mapping[direction]

        xs.append(x)
        ys.append(y)

        marbles[(x, y)] = (number, weight, direction)

    max_time = max(
        max(xs) - min(xs),
        max(ys) - min(ys)
    )

    last_time = -1

    for time in range(1, max_time + 1):

        if len(marbles) <= 1:
            break

        temp = {}
        collision = False

        for pos, marble in marbles.items():

            x, y = pos
            number, weight, direction = marble

            nx = x + dxs[direction]
            ny = y + dys[direction]

            if (nx, ny) not in temp:
                temp[(nx, ny)] = marble

            else:
                collision = True

                old_number, old_weight, old_direction = temp[(nx, ny)]

                if weight > old_weight or \
                   (weight == old_weight and number > old_number):

                    temp[(nx, ny)] = marble

        if collision:
            last_time = time

        marbles = temp

    print(last_time)