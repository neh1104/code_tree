n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.

class Std():
    def __init__(self, name, s1, s2, s3):
        self.name, self.s1, self.s2, self.s3 = name, s1, s2, s3

std = [Std(name[i], score1[i], score2[i], score3[i]) for i in range(n)]

std.sort(key = lambda x : x.s1 +x.s2 +x.s3)

for i in range(n):
    print(std[i].name, std[i].s1, std[i].s2, std[i].s3)
    