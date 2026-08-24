# 변수 선언 및 입력:
n, m, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
pieces = [1 for _ in range(k)]

ans = 0


# 점수를 계산합니다.
def calc():
    score = 0
    for piece in pieces:
        score += (piece >= m)
    
    return score


def find_max(cnt):
    global ans
    
    # 말을 직접 n번 움직이지 않아도
    # 최대가 될 수 있으므로 항상 답을 갱신합니다.
    ans = max(ans, calc())
    
    # 더 이상 움직일 수 없으면 종료합니다.
    if cnt == n: 
        return
    
    for i in range(k):
        # 움직여서 더 이득이 되지 않는
        # 말은 더 이상 움직이지 않습니다.
        if pieces[i] >= m:
            continue
        
        pieces[i] += nums[cnt]
        find_max(cnt + 1)
        pieces[i] -= nums[cnt]


find_max(0)
print(ans)
