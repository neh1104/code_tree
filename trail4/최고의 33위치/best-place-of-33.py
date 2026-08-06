n = int(input())
a = [
    list(map(int, input().split())) for _ in range(n)
]
#print(a)
MAX = 0
for i in range(n-2):
    for j in range(n-2):
        sum = 0
        for I in range(3):
            for J in range(3):
                sum += int(a[i+I][j+J])

        MAX = max(MAX, sum)

print(MAX)