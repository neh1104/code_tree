N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.

ls = [K] * N
idx = -1
for i in student:
    ls[i-1] -= 1
    if ls.count(0) >= 1:
        idx = i
        break
print(idx)