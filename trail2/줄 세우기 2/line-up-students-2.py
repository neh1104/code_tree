n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.

students.sort(key = lambda x: (x[0], -x[1]))

for x in students:
    print(x[0], x[1], x[2])