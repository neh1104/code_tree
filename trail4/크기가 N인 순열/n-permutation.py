n = int(input())

visited = [False] * (n + 1)  # 숫자의 사용 여부 체크
arr = []                     # 현재 만들어지고 있는 순열

def choose(curr_num):
    # N개의 숫자를 모두 골랐다면 출력 후 종료
    if curr_num == n + 1:
        print(*arr)
        return

    # 1부터 N까지 순서대로 탐색 (사전순 출력을 보장)
    for i in range(1, n + 1):
        if not visited[i]:      # 아직 사용하지 않은 숫자라면
            visited[i] = True   # 사용 처리
            arr.append(i)
            
            choose(curr_num + 1) # 다음 위치의 숫자 정하러 재귀 호출
            
            arr.pop()           # 원상복구 (백트래킹)
            visited[i] = False

choose(1)