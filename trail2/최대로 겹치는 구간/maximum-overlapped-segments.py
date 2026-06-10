n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

ls = [0]*200

for i in segments:
    a = i[0]+100; b = i[1]+100
    for j in range(a, b):
        ls[j] += 1

print(max(ls))