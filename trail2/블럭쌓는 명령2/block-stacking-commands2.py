n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
ls = [0]*n

for i in commands:

    a = min(i)-1; b = max(i)
    for j in range(a, b):
        ls[j] += 1


print(max(ls))