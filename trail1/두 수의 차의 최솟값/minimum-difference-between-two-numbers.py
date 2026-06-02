n = int(input())
arr = list(map(int, input().split()))

diff = 100
for i in arr:
    for j in arr:
        if abs(i-j) < diff and i != j:
            diff = abs(i-j)

print(diff)