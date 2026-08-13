n = int(input())

visited = [False] * (n + 1)
arr = []

def choose(curr_num):
    if curr_num == n + 1:
        print(*arr)
        return

    # N부터 1까지 역순으로 탐색 (거꾸로 순열)
    for i in range(n, 0, -1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            
            choose(curr_num + 1)
            
            arr.pop()
            visited[i] = False

choose(1)