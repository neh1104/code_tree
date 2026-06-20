N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
MAX = -1
def in_range(x):
    return x < N

for i in range(N):
    for j in range(1, K+1):
        if in_range(i+j) and num[i] == num[i+j]:
            MAX = max(MAX, num[i])

print(MAX)