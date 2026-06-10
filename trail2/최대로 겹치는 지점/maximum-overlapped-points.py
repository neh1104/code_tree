n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

ls = [0]*(101)

for tup in segments:
    a = tup[0]; b = tup[1]+1
    for i in range(a, b):
        ls[i] += 1
print(max(ls))