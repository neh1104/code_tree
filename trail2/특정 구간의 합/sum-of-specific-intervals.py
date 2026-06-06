n, m = map(int, input().split())
arr = list(map(int, input().split()))
q = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def ssum(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += arr[i-1]
    return sum

for A, B in q:
    print(ssum(A, B))