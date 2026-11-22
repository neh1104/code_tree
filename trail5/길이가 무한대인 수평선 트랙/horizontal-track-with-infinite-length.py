from sortedcontainers import SortedSet

# 변수 선언 및 입력:
n, t = tuple(map(int, input().split()))
x, v = [], []
for _ in range(n):
    input_x, input_v = tuple(map(int, input().split()))
    x.append(input_x)
    v.append(input_v)

# x 순으로 정렬하여 사람들을 관리합니다.
people_x = SortedSet()
# 인접한 사람끼리 만나는 시간 순으로 정렬하여 사건들을 관리합니다.
event_t = SortedSet()


# (x1, v1) 사람이 바로 앞에 있는 (x2, v2)와 마주치는 데 걸리는 시간
# 정보를 얻어 사건 정보를 추가합니다. 
def add_event(x1, v1, x2, v2):
    # 절대 따라잡을 수 없는 경우라면 무시합니다.
    if v1 <= v2:
        return
        
    event_t.add((1.0 * (x2 - x1) / (v1 - v2), x1, v1))


# (x1, v1) 사람이 바로 앞에 있는 (x2, v2)와 마주치는 데 걸리는 시간
# 정보를 얻어 해당 사건 정보를 제거합니다.
def remove_event(x1, v1, x2, v2):
    # 절대 따라잡을 수 없는 경우라면 무시합니다.
    if v1 <= v2:
        return
    
    event_t.remove((1.0 * (x2 - x1) / (v1 - v2), x1, v1))

   
# 사람들을 set으로 관리합니다.
for i in range(n):
    people_x.add((x[i], v[i]))

# 인접한 사람끼리 만나는 사건도 set으로 관리합니다.
# (t, x, v) : 
# 현재 x 위치에서 속도 v로 이동하는 사람과
# 바로 앞에 있는 사람이 
# 마주치는 데 거리는 시간 t라는 정보 기입
for i in range(n - 1):
    add_event(x[i], v[i], x[i + 1], v[i + 1])

# 앞지르는 사건이 존재한다면 반복합니다.
while event_t:
    curr_t, x, v = event_t[0]

    # 이미 t분이 넘었다면 종료합니다.
    if curr_t > t:
        break

    # 해당 사람과 사건을 삭제합니다.
    people_x.remove((x, v))
    event_t.remove((curr_t, x, v))
    
    # 바로 앞 사람 위치를 구합니다.
    index = people_x.bisect_right((x, v))
    nx, nv = people_x[index]

    # 바로 뒤에 사람이 있다면 
    # 이전 사건을 삭제하고
    # 새로운 사건을 추가합니다.
    if index != 0:
        index -= 1
        px, pv = people_x[index]
        remove_event(px, pv, x, v)
        add_event(px, pv, nx, nv)

# 서로 다른 그룹의 수를 출력합니다.
print(len(people_x))
