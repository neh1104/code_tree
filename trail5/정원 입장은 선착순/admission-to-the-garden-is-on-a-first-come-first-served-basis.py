import heapq
import sys

input = sys.stdin.readline


def solve():
  n = int(input().strip())
  people = []

  for idx in range(1, n + 1):
    a, t = map(int, input().split())
    # (도착 시간, 번호표, 체류 시간)
    people.append((a, idx, t))

  # 1. 도착 시간 기준으로 오름차순 정렬
  people.sort(key=lambda x: x[0])

  pq = []  # 대기 중인 사람들: (번호표, 도착 시간, 체류 시간)
  cur_time = 0
  ptr = 0
  max_wait = 0

  while ptr < n or pq:
    # 대기열이 비어 있고 현재 시각보다 늦게 도착하는 다음 사람이 있다면 시각 점프
    if not pq and ptr < n and cur_time < people[ptr][0]:
      cur_time = people[ptr][0]

    # 현재 시각 이하에 도착한 모든 사람을 대기 힙에 추가
    while ptr < n and people[ptr][0] <= cur_time:
      a, idx, t = people[ptr]
      heapq.heappush(pq, (idx, a, t))
      ptr += 1

    # 번호표가 가장 작은 사람 입장
    idx, a, t = heapq.heappop(pq)
    wait_time = cur_time - a
    if wait_time > max_wait:
      max_wait = wait_time

    # 정원에 머무는 시간만큼 현재 시각 진행
    cur_time += t

  print(max_wait)


if __name__ == "__main__":
  solve()