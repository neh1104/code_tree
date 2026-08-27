n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
vt = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)
#print(graph)

cnt = 0
def dfs(curr):
    global cnt
    
    for nxt in graph[curr]:
        if vt[nxt] == 1:
            continue
        cnt += 1
        vt[nxt] = 1
        dfs(nxt)
vt[1] = 1
dfs(1)
print(cnt)